import re

from typing import List

from src.base.animevost import schemas
from src.base.utils import cash_memory
from src.anime import models


class WriteDB:
    """Запись в БД"""
    @cash_memory
    def _write_genre(self, genre_sting: str) -> models.Genre:
        """Запись жанров"""
        return models.Genre.objects.create(title=genre_sting)

    def clear_cash_memory(self):
        """Очистка кеша-жанров"""
        self._write_genre.cache_clear()

    def _write_screen_images(self, screen_images: str) -> models.ScreenImages:
        """Запись в таблицу ScreenImages"""
        return models.ScreenImages.objects.create(images=screen_images)

    def _write_anime(
            self,
            anime_data: schemas.AnimeData,
            day: str = ''
    ) -> models.Anime:
        """Запись в таблицу Anime"""
        anons = True if re.search(r'Анонс', anime_data.title) else False
        anime = models.Anime.objects.create(
            id_anime=anime_data.id,
            title=anime_data.title,
            link=anime_data.link,
            rating=anime_data.rating,
            votes=anime_data.votes,
            description=anime_data.description,
            director=anime_data.director,
            url_image_preview=anime_data.url_image_preview,
            year=anime_data.year,
            timer=anime_data.timer,
            type=anime_data.type,
            day_week=day,
            anons=anons
        )
        return anime

    def _write_anime_composed(
            self,
            base_anime: models.Anime,
            anime_composed_list: List[schemas.AnimeData]
    ) -> None:
        """Запись в поле Anime.anime_composed"""
        if anime_composed_list:
            for anime_schemas in anime_composed_list:
                anime_composed = self.write_anime(anime_schemas)
                base_anime.anime_composed.add(anime_composed)

    def write_anime(
            self,
            anime_data: schemas.AnimeData,
            day: str = ''
    ) -> models.Anime:
        """Запись дынных аниме"""
        anime_db = self._write_anime(anime_data, day)

        if anime_data.screen_image:
            for screen in anime_data.screen_image:
                screen_db = self._write_screen_images(screen)
                anime_db.screen_image.add(screen_db)

        if anime_data.genre:
            for genre in anime_data.genre.split(', '):
                genre_db = self._write_genre(genre)
                anime_db.genre.add(genre_db)

        return anime_db

    def write_anime_schedule(
            self,
            anime_data: dict[str: List[schemas.AnimeFull]]
    ) -> None:
        """Запись дынных аниме расписание"""
        for key, value in anime_data.items():
            for anime_schemas in value:
                anime = self.write_anime(anime_schemas, key)
                self._write_anime_composed(anime, anime_schemas.anime_composed)

    def write_anime_anons(self, anime_data: List[schemas.AnimeFull]):
        """Запись дынных аниме анонс"""
        anons_list = models.Anime.objects.filter(anons=True).\
            values_list('id_anime', flat=True)
        for anime_schemas in anime_data:
            if anime_schemas.id not in anons_list:
                anime = self.write_anime(anime_schemas)
                self._write_anime_composed(anime, anime_schemas.anime_composed)

    def write_anime_full(self, anime_data: schemas.AnimeFull):
        """Запись аниме с Anime.anime_composed"""
        if not models.Anime.objects.filter(id_anime=anime_data.id).exists():
            anime = self.write_anime(anime_data)
            self._write_anime_composed(anime, anime_data.anime_composed)
