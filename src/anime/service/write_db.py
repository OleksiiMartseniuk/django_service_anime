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

    def _write_screen_images(self, screen_images: str) -> models.ScreenImages:
        """Запись в таблицу ScreenImages"""
        return models.ScreenImages.objects.create(images=screen_images)

    def _write_anime(
            self, anime_data: schemas.AnimeData, day: str = ''
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

    def write_anime_all(self, anime_data: dict[str: List[schemas.AnimeFull]]):
        """Запись дынных аниме расписание"""
        for key, value in anime_data.items():
            for anime in value:
                anime_db = self._write_anime(anime, key)

                if anime.screen_image:
                    for screen in anime.screen_image:
                        screen_db = self._write_screen_images(screen)
                        anime_db.screen_image.add(screen_db)

                if anime.genre:
                    for genre in anime.genre.split(' '):
                        genre_db = self._write_genre(genre)
                        anime_db.genre.add(genre_db)
