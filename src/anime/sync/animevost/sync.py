import logging
import time
import itertools

from django.db import transaction
from django.db.models import Q
from django_db_logger.models import StatusLog

from src.anime.models import AnimeVost, Genre, ScreenImages
from src.anime.utils import download_image
from src.utils.animevost.api import ApiAnimeVostClient
from src.utils.animevost.parser import ParserClient

from .exception import AnimeVostExists


logger = logging.getLogger("db")


class AnimeVostSync:
    def __init__(self):
        self.report_updated = []
        self.report_created = []
        self.api_vost_client = ApiAnimeVostClient()
        self.parser = ParserClient(logger=logger)

    def sync(self):
        self.sync_schedule()

    def sync_schedule(self):
        start_sync_schedule_time = time.time()
        try:
            anime_schedule_data = self.parser.get_schedule()
        except Exception as ex:
            logger.error("Parser Error", exc_info=ex)
            return None
        anime_ids = []
        for day_name, anime_week in anime_schedule_data.items():
            for anime in anime_week:
                anime_ids.append(anime.id_anime)
                if anime.anime_composed:
                    for anime_c in anime.anime_composed:
                        anime_ids.append(anime_c.id_anime)
        anime_exists_ids = self.get_anime_exists(anime_ids)

        anime_create_ids, anime_update_ids = [], []
        for day_name, anime_week in anime_schedule_data.items():
            for anime in anime_week:
                anime_composed_create_list = []
                if anime.id_anime in anime_exists_ids:
                    anime_update_ids.append(anime.id_anime)
                else:
                    anime_composed_create_list.append(anime.id_anime)
                if anime.anime_composed:
                    for anime_c in anime.anime_composed:
                        if anime_c.id_anime in anime_exists_ids:
                            anime_update_ids.append(anime_c.id_anime)
                        else:
                            anime_composed_create_list.append(anime_c.id_anime)
                if anime_composed_create_list:
                    anime_create_ids.append(anime_composed_create_list)

        anime_create_list_ids = list(itertools.chain(*anime_create_ids))
        if anime_create_list_ids or anime_update_ids:
            AnimeVost.objects.filter(
                ~Q(anime_id__in=[*anime_create_list_ids, *anime_update_ids]),
            ).update(day_week=None)

        anime_created_quantity = len(anime_create_list_ids)
        anime_create_errors = 0
        for anime_composed_create_list in anime_create_ids:
            anime_list_objs = []
            for anime_id in anime_composed_create_list:
                try:
                    anime = self.create_anime(anime_id=anime_id)
                except Exception as ex:
                    anime_create_errors += 1
                    logger.error(
                        f"Anime [{anime_id}] was not created",
                        exc_info=ex,
                    )
                else:
                    anime_list_objs.append(anime)
            # TODO: take into account those anime that are already in the heap
            for anime_base in anime_list_objs:
                for anime_clone in anime_list_objs:
                    if anime_base.id != anime_clone.id:
                        anime_base.anime_composed.add(anime_clone)

        anime_updated_quantity = len(anime_update_ids)
        anime_update_errors = 0
        for anime_update_id in anime_update_ids:
            try:
                self.update_anime(anime_id=anime_update_id)
            except Exception as ex:
                anime_update_errors += 1
                logger.error(
                    f"Anime [{anime_update_id}] was not updated",
                    exc_info=ex
                )

        end_sync_schedule_time = time.time() - start_sync_schedule_time
        msg = (
            "Report Sync Schedule\n"
            f"Time: {int(end_sync_schedule_time)}s\n"
        )
        if anime_created_quantity:
            msg += (
                f"{'=' * 40}\n"
                f"- Anime created {len(self.report_created)}/"
                f"{anime_created_quantity}\n"
                f"- Anime create error {anime_create_errors}\n"
                f"- Anime create list:\n"
                f"{self.get_report_items_list(self.report_created)}\n"
            )
        if anime_updated_quantity:
            msg += (
                f"{'=' * 40}\n"
                f"- Anime updated {len(self.report_updated)}/"
                f"{anime_updated_quantity}\n"
                f"- Anime update error {anime_update_errors}\n"
                f"- Anime update list:\n"
                f"{self.get_report_items_list(self.report_updated)}\n"
            )
        StatusLog.objects.create(
            logger_name="db",
            level=logging.INFO,
            msg="Report",
            trace=msg,
        )

    @staticmethod
    def get_report_items_list(items: list) -> str:
        str_items = ""
        for i, w in enumerate(items, 1):
            if not i % 10:
                str_items += "\n"
            str_items += f"{w}, "
        return str_items

    @staticmethod
    def get_anime_exists(anime_ids: list) -> list:
        anime_exists_ids = AnimeVost.objects.filter(
            anime_id__in=anime_ids,
        ).values_list("anime_id", flat=True)
        return list(anime_exists_ids)

    @transaction.atomic
    def create_anime(self, anime_id: int) -> AnimeVost:
        if AnimeVost.objects.filter(anime_id=anime_id).exists():
            raise AnimeVostExists(
                f"AnimeVost[{anime_id}] exists and dont be create",
            )

        anime_dict = self.api_vost_client.get_anime(anime_id=anime_id).dict()
        screen_image = anime_dict.pop("screen_image", None)
        url_image_preview = anime_dict.pop("url_image_preview", None)
        genres = anime_dict.pop("genres", None)
        anime_dict["anime_id"] = anime_dict.pop("id")
        anime_dict["day_week"] = anime_dict.pop("day", None)

        anime = AnimeVost.objects.create(**anime_dict)

        download_image(
            obj_image=anime.url_image_preview,
            image_url=url_image_preview,
        )
        self.__create_genres(genres_title=genres, anime=anime)
        self.__create_screen_images(
            screen_images=screen_image,
            anime=anime,
        )
        # TODO: Add series for anime
        self.report_created.append(anime.id)
        return anime

    @staticmethod
    def __create_genres(genres_title: list[str], anime: AnimeVost) -> None:
        for title in genres_title:
            genre, _ = Genre.objects.get_or_create(title=title)
            anime.genre.add(genre)

    @staticmethod
    def __create_screen_images(
        screen_images: list[str],
        anime: AnimeVost,
    ) -> None:
        for screen_image in screen_images:
            obj = ScreenImages.objects.create()
            download_image(obj_image=obj.images, image_url=screen_image)
            anime.screen_image.add(obj)

    @transaction.atomic
    def update_anime(self, anime_id: int):
        anime: AnimeVost | None = AnimeVost.objects.filter(
            anime_id=anime_id,
        ).first()
        if anime is None:
            raise AnimeVostExists(
                f"AnimeVost[{anime_id}] dont exists and dont be updated",
            )

        anime_dict = self.api_vost_client.get_anime(anime_id=anime_id).dict()
        anime_dict["day_week"] = anime_dict.pop("day", None)
        screen_image = anime_dict.pop("screen_image", None)
        url_image_preview = anime_dict.pop("url_image_preview", None)
        anime_dict.pop("genres", None)
        anime_dict.pop("id", None)

        if not anime.url_image_preview and url_image_preview:
            download_image(
                obj_image=anime.url_image_preview,
                image_url=url_image_preview,
            )
        if not anime.screen_image.count() and screen_image:
            self.__create_screen_images(
                screen_images=screen_image,
                anime=anime,
            )

        for field, value in anime_dict.items():
            if hasattr(anime, field):
                setattr(anime, field, value)
        anime.save()
        # TODO: Add update series for anime
        self.report_updated.append(anime.id)
# from src.anime.sync.animevost.sync import AnimeVostSync
# s = AnimeVostSync()
# s.sync()