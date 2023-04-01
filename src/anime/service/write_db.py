import re

from typing import List

from django.db.models import Q

from src.anime.service.utils import get_number, download_image, get_series_link
from src.base.animevost import schemas
from src.anime import models


class WriteDB:
    """Запись в БД"""
    def _write_genre(self, genre_sting: str) -> models.Genre:
        """Запись жанров"""
        genre, _ = models.Genre.objects.get_or_create(title=genre_sting)
        return genre

    def _write_screen_images(self, screen_images: str) -> models.ScreenImages:
        """Запись в таблицу ScreenImages"""
        obj = models.ScreenImages.objects.create()
        # Скачивания изображения
        download_image(obj.images, screen_images)
        return obj

    def _write_anime(
            self,
            anime_data: schemas.AnimeData,
            day: str = None,
            indefinite_exit: bool = False
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
            year=anime_data.year,
            timer=anime_data.timer,
            type=anime_data.type,
            day_week=day,
            anons=anons,
            indefinite_exit=indefinite_exit
        )
        # Скачивания изображения
        if not anime.url_image_preview:
            download_image(
                anime.url_image_preview,
                anime_data.url_image_preview
            )
        return anime

    def _write_anime_composed(
            self,
            base_anime: models.Anime,
            anime_list: List[schemas.AnimeData],
            update: bool = False
    ) -> None:
        """Запись в поле Anime.anime_composed"""
        if anime_list:
            obj_lit = [
                self.write_anime(sch, update=update) for sch in anime_list
            ]
            obj_lit.append(base_anime)
            for obj_main in obj_lit:
                for obj1_composed in obj_lit:
                    if obj_main.id != obj1_composed.id:
                        obj_main.anime_composed.add(obj1_composed)

    def write_anime(
            self,
            anime_data: schemas.AnimeData,
            day: str = None,
            update: bool = False,
            indefinite_exit: bool = False
    ) -> models.Anime:
        """Запись дынных аниме"""
        # При обновлении Anime.anime_composed сначала ищем в db на совпадения
        # если значения найдено возвращаем obj[Anime]
        if update:
            if models.Anime.objects.filter(id_anime=anime_data.id).exists():
                return models.Anime.objects.get(id_anime=anime_data.id)

        anime_db = self._write_anime(anime_data, day, indefinite_exit)

        if anime_data.screen_image:
            for screen in anime_data.screen_image:
                screen_db = self._write_screen_images(screen)
                anime_db.screen_image.add(screen_db)

        if anime_data.genre:
            for genre in re.split(r', |\. ', anime_data.genre):
                genre_db = self._write_genre(genre)
                anime_db.genre.add(genre_db)

        return anime_db

    def write_anime_schedule(
            self,
            anime_data: dict[str: List[schemas.AnimeFull]]
    ) -> None:
        """Запись дынных аниме расписание"""
        anons_list = models.Anime.objects.filter(~Q(day_week=None)).\
            values_list('id_anime', flat=True)
        for key, value in anime_data.items():
            for anime_schemas in value:
                if anime_schemas.id not in anons_list:
                    anime = self.write_anime(anime_schemas, key)
                    self._write_anime_composed(
                        anime,
                        anime_schemas.anime_composed
                    )

    def write_anime_anons(self, anime_data: List[schemas.AnimeFull]) -> None:
        """Запись дынных аниме анонс"""
        anons_list = models.Anime.objects.filter(anons=True).\
            values_list('id_anime', flat=True)
        for anime_schemas in anime_data:
            if anime_schemas.id not in anons_list and \
                    re.search(r'Анонс', anime_schemas.title):
                anime = self.write_anime(anime_schemas)
                self._write_anime_composed(anime, anime_schemas.anime_composed)

    def write_anime_full(
            self,
            anime_data: schemas.AnimeFull,
            day: str = None,
            indefinite_exit: bool = False
    ) -> None:
        """Запись аниме с Anime.anime_composed"""
        if not models.Anime.objects.filter(id_anime=anime_data.id).exists():
            anime = self.write_anime(
                anime_data,
                day,
                indefinite_exit=indefinite_exit
            )
            self._write_anime_composed(
                anime,
                anime_data.anime_composed,
                update=True
            )

    def write_series(self, id: int, series_data: List[schemas.Series]) -> None:
        """Запись серий"""
        objs = []
        for date in series_data:
            objs.append(
                models.Series(
                    id_anime=id,
                    **date.dict(),
                    number=get_number(date.name),
                    link=get_series_link(date.serial)
                )
            )
        models.Series.objects.bulk_create(objs)
