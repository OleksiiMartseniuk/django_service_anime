import logging
import time

from django.db import transaction
from django.db.models import Q
from django_db_logger.models import StatusLog

from src.anime.models import AnimeVost, Genre, ScreenImages
from src.anime.utils import download_image
from src.utils.animevost.api import ApiAnimeVostClient
from src.utils.animevost.parser import ParserClient
from src.utils.animevost.schemas import AnimeMin

from .exception import AnimeVostExists


logger = logging.getLogger("db")


class AnimeVostSync:
    def __init__(self):
        self.report_updated = []
        self.report_created = []
        self.api_vost_client = ApiAnimeVostClient()
        self.parser = ParserClient(logger=logger)

    def sync(self):
        start_sync_time = time.time()
        report_sync_schedule = self.sync_schedule()
        report_sync_anons = self.sync_anons()
        end_sync_time = time.time() - start_sync_time
        msg = (
            "Report Sync AnimeVost\n"
            f"Time: {int(end_sync_time)}s\n"
        )
        if report_sync_schedule:
            msg += report_sync_schedule
        if report_sync_anons:
            msg += report_sync_anons
        if self.report_created:
            msg += (
                f"\n- Anime create list:\n"
                f"{self.get_report_items_list(self.report_created)}\n"
            )
        if self.report_updated:
            msg += (
                f"\n- Anime update list:\n"
                f"{self.get_report_items_list(self.report_updated)}\n"
            )
        StatusLog.objects.create(
            logger_name="db",
            level=logging.INFO,
            msg="Report Sync",
            trace=msg,
        )

    def sync_anons(self):
        try:
            anime_anons_data = self.parser.get_anons()
        except Exception as ex:
            logger.error("Parser Error", exc_info=ex)
            return None
        if anime_anons_data is None:
            logger.info("Data anime anons don't exist.")
            return None

        anime_ids, anime_ids_full_composition = (
            self.get_anime_ids_with_parser(anime_anons_data)
        )
        anime_exists_ids = self.get_anime_exists(anime_ids)
        anime_create_ids, anime_update_ids = (
            self.get_items_ids_create_and_update(
                anime_list=anime_anons_data,
                anime_exists_ids=anime_exists_ids,
            )
        )
        anime_created_quantity = len(anime_create_ids)
        anime_created_success = 0
        anime_create_errors = 0
        for anime_id in anime_create_ids:
            try:
                self.create_anime(anime_id=anime_id)
            except Exception as ex:
                anime_create_errors += 1
                logger.error(
                    f"Anime [{anime_id}] was not created",
                    exc_info=ex,
                )
            else:
                anime_created_success += 1
        self.__set_anime_composed(anime_ids_full_composition)

        anime_updated_quantity = len(anime_update_ids)
        anime_updated_success = 0
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
            else:
                anime_updated_success += 1

        report = self.get_report(
            "Anons",
            anime_created_quantity,
            anime_created_success,
            anime_create_errors,
            anime_updated_quantity,
            anime_updated_success,
            anime_update_errors,
        )
        return report

    def sync_schedule(self) -> str | None:
        try:
            anime_schedule_data = self.parser.get_schedule()
        except Exception as ex:
            logger.error("Parser Error", exc_info=ex)
            return None

        anime_schedule_data_list = []
        for items in anime_schedule_data.values():
            for item in items:
                anime_schedule_data_list.append(item)

        anime_ids, anime_ids_full_composition = (
            self.get_anime_ids_with_parser(anime_schedule_data_list)
        )
        anime_exists_ids = self.get_anime_exists(anime_ids)
        anime_create_ids, anime_update_ids = (
            self.get_items_ids_create_and_update(
                anime_list=anime_schedule_data_list,
                anime_exists_ids=anime_exists_ids,
            )
        )

        if anime_create_ids or anime_update_ids:
            AnimeVost.objects.filter(
                ~Q(anime_id__in=[*anime_create_ids, *anime_update_ids]),
                day_week__isnull=False,
            ).update(day_week=None)

        anime_created_quantity = len(anime_create_ids)
        anime_created_success = 0
        anime_create_errors = 0
        for anime_id in anime_create_ids:
            try:
                self.create_anime(anime_id=anime_id)
            except Exception as ex:
                anime_create_errors += 1
                logger.error(
                    f"Anime [{anime_id}] was not created",
                    exc_info=ex,
                )
            else:
                anime_created_success += 1
        self.__set_anime_composed(anime_list=anime_ids_full_composition)

        anime_updated_quantity = len(anime_update_ids)
        anime_updated_success = 0
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
            else:
                anime_updated_success += 1
        report = self.get_report(
            "Schedule",
            anime_created_quantity,
            anime_created_success,
            anime_create_errors,
            anime_updated_quantity,
            anime_updated_success,
            anime_update_errors,
        )
        return report

    @staticmethod
    def get_report(
        title: str,
        anime_created_quantity: int,
        anime_created_success: int,
        anime_create_errors: int,
        anime_updated_quantity: int,
        anime_updated_success: int,
        anime_update_errors: int,
    ):
        msg = f"\nReport Sync {title}\n"
        if anime_created_quantity:
            msg += (
                f"{'=' * 40}\n"
                f"- Anime created {anime_created_success}/"
                f"{anime_created_quantity}\n"
                f"- Anime create error {anime_create_errors}\n"
            )
        if anime_updated_quantity:
            msg += (
                f"{'=' * 40}\n"
                f"- Anime updated {anime_updated_success}/"
                f"{anime_updated_quantity}\n"
                f"- Anime update error {anime_update_errors}\n"
            )
        return msg

    @staticmethod
    def __set_anime_composed(anime_list: list[list[int]]):
        for anime_ids in anime_list:
            anime_exist = AnimeVost.objects.filter(anime_id__in=anime_ids)
            for anime in anime_exist:
                for anime_c in anime_exist.exclude(id=anime.id):
                    anime.anime_composed.add(anime_c)

    @staticmethod
    def find_full_composition_anime(
        anime_vost_id: int,
        anime_list: list[list[int]],
    ):
        for anime_ids in anime_list:
            if anime_vost_id in anime_ids:
                return AnimeVost.objects.filter(anime_id__in=anime_ids)
        return list()

    @staticmethod
    def get_items_ids_create_and_update(
        anime_list: list[AnimeMin],
        anime_exists_ids: list[int],
    ) -> tuple[list, list]:
        anime_create_ids, anime_update_ids = [], []
        for anime in anime_list:
            if anime.id_anime in anime_exists_ids:
                anime_update_ids.append(anime.id_anime)
            else:
                anime_create_ids.append(anime.id_anime)
            if anime.anime_composed:
                for anime_c in anime.anime_composed:
                    if anime_c.id_anime in anime_exists_ids:
                        anime_update_ids.append(anime_c.id_anime)
                    else:
                        anime_create_ids.append(anime_c.id_anime)
        return anime_create_ids, anime_update_ids

    @staticmethod
    def get_anime_ids_with_parser(
        anime_list: list[AnimeMin],
    ) -> tuple[list, list]:
        anime_ids = []
        anime_ids_full_composition = []
        for anime in anime_list:
            anime_composed_ids = [anime.id_anime]
            if anime.anime_composed:
                for anime_c in anime.anime_composed:
                    anime_composed_ids.append(anime_c.id_anime)
            anime_ids_full_composition.append(anime_composed_ids)
            anime_ids += anime_composed_ids
        return anime_ids, anime_ids_full_composition

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
    def create_anime(self, anime_id: int) -> None:
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
