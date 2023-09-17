import logging
from collections import defaultdict

from django.db import transaction

from src.anime.models import AnimeVost, Genre, ScreenImages
from src.anime.utils import download_image
from src.utils.animevost.api import ApiAnimeVostClient
from src.utils.animevost.parser import ParserClient

from .exception import AnimeVostExists


logger = logging.getLogger('db')


class AnimeVostSync:
    def __init__(self):
        self.report_updated = []
        self.report_created = []

    def sync(self):
        parser = ParserClient()
        self.sync_schedule(parser=parser)
        # parser.get_schedule()
        # anime_exists_ids = self.get_anime_exists(anime_ids)
        # from src.anime.sync.animevost.sync import AnimeVostSync

    def sync_schedule(self, parser: ParserClient):
        anime_schedule_data = parser.get_schedule()
        anime_ids = []
        for day_name, anime_week in anime_schedule_data.items():
            for anime in anime_week:
                anime_ids.append(anime.id_anime)
                if anime.anime_composed:
                    for anime_c in anime.anime_composed:
                        anime_ids.append(anime_c.id_anime)
        anime_exists_ids = self.get_anime_exists(anime_ids)
        # TODO: think about it
        anime_create_ids = defaultdict(list)
        anime_update_ids = list()
        for day_name, anime_week in anime_schedule_data.items():
            for anime in anime_week:
                if anime.id_anime in anime_exists_ids:
                    anime_update_ids.append(anime.id_anime)
                else:
                    anime_create_ids[anime.id_anime]
                if anime.anime_composed:
                    for anime_c in anime.anime_composed:
                        if anime_c.id_anime in anime_exists_ids:
                            anime_update_ids.append(anime_c.id_anime)
                        else:
                            anime_create_ids[anime.id_anime].append(
                                anime_c.id_anime,
                            )
        for anime_base_id, anime_consists in anime_create_ids.items():
            self.__create_anime_composed(
                anime_base=anime_base_id,
                anime_consists=anime_consists,
            )

    @staticmethod
    def get_anime_exists(anime_ids: list) -> list:
        anime_exists_ids = AnimeVost.objects.filter(
            anime_id__in=anime_ids,
        ).values_list('anime_id', flat=True)
        return list(anime_exists_ids)

    def __create_anime_composed(
        self,
        anime_base: int,
        anime_consists: list[int | None]
    ) -> None:
        # нужно сделать так чтобы в каждом аниме были ссылки остальные в другое которое в ходит в него
        # переделать этот метод (возможен кей в котором мы передайом лист котором все анеме которые нужно обеденить)
        anime_list = []
        try:
            anime = self.create_anime(anime_id=anime_base)
        except Exception as ex:
            logger.error(
                f'Anime_Base[{anime_base}] Anime_Compose'
                f'[{anime_consists}] [BASE]',
                exc_info=ex,
            )
        else:
            if anime_consists:
                for anime_composed_id in anime_consists:
                    try:
                        anime_composed = self.create_anime(
                            anime_id=anime_composed_id,
                        )
                    except Exception as ex:
                        logger.error(
                            f'Anime [{anime_composed_id}] [COMPOSED]',
                            exc_info=ex,
                        )
                    else:
                        anime.anime_composed.add(anime_composed)

    @transaction.atomic
    def create_anime(
        self,
        anime_id: int,
        indefinite_exit: bool = False
    ) -> AnimeVost:
        if AnimeVost.objects.filter(anime_id=anime_id).exists():
            raise AnimeVostExists(
                f"AnimeVost[{anime_id}] exists and dont be create",
            )
        api_anime_vost_client = ApiAnimeVostClient()
        anime_data = api_anime_vost_client.get_anime(anime_id=anime_id)

        anime = AnimeVost.objects.create(
            anime_id=anime_data.id,
            title_en=anime_data.title_en,
            title_ru=anime_data.title_ru,
            rating=anime_data.rating,
            votes=anime_data.votes,
            description=anime_data.description,
            director=anime_data.director,
            year=anime_data.year,
            timer=anime_data.timer,
            type=anime_data.type,
            anons=anime_data.anons,
            day_week=anime_data.day,
            indefinite_exit=indefinite_exit,
        )
        download_image(
            obj_image=anime.url_image_preview,
            image_url=anime_data.url_image_preview,
        )
        self.__create_genres(genres_title=anime_data.genres, anime=anime)
        self.__create_screen_images(
            screen_images=anime_data.screen_image,
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

    def update_anime(self, anime_id: int):
        pass

