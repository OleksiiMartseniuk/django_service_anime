from django.db import transaction

from src.anime.models import AnimeVost, Genre, ScreenImages
from src.anime.utils import download_image
from src.utils.animevost.api import ApiAnimeVostClient

from .exception import AnimeVostExists


class AnimeVostSync:
    def __init__(self):
        self.update_report = []
        self.create_report = []

    @transaction.atomic
    def create(self, anime_id: int, indefinite_exit: bool = False):
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
        self.create_report.append(anime_id)

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

    def update(self, anime_id: int):
        pass

