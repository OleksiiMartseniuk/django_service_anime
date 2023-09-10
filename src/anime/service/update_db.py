import logging
import re

from dataclasses import dataclass
from typing import List

from src.anime.service.utils import get_number, get_series_link
from src.utils.animevost import schemas
from src.anime.models import Anime, Series

from django.db.models import Q
from django.utils import timezone

from .write_db import WriteDB


logger = logging.getLogger('main')


@dataclass
class AnimeMini:
    """Мини описания аниме"""
    id: int
    link: str
    day: str | None = None


class UpdateDataParser:
    """Обновления данных Parser"""
    def _create_schemas(
        self,
        id: int,
        link: str,
        day: str | None = None
    ) -> AnimeMini:
        """Создать схему AnimeComposed"""
        return AnimeMini(id=id, link=link, day=day)

    def _update_anime(
            self,
            anime_data: schemas.AnimeData | schemas.Anime,
            day: str | None = None
    ) -> bool:
        """Обновления данных anime"""
        anons = True if re.search(r'Анонс', anime_data.title) else False
        try:
            anime = Anime.objects.get(id_anime=anime_data.id)
            anime.title = anime_data.title
            anime.rating = anime_data.rating
            anime.votes = anime_data.votes
            anime.timer = anime_data.timer
            anime.day_week = day
            anime.anons = anons
            anime.updated = timezone.now()
            anime.save()

            # обновления скриншотов (если их не было)
            if not anime.screen_image.count() and anime_data.screen_image:
                for screen in anime_data.screen_image:
                    screen_db = WriteDB()._write_screen_images(screen)
                    anime.screen_image.add(screen_db)
            return True
        except Anime.DoesNotExist:
            logger.debug(
                f"Новое аниме id_anime[{anime_data.id}] нужно записать."
            )
            return False

    def update_anime_schedule(
        self,
        anime_data: dict[str, List[schemas.AnimeFull]]
    ) -> None | List[AnimeMini]:
        """Обновления данных schedule"""
        # Список до записи
        write_list = []
        # Список всех принятых anime id
        id_list = []
        for key, value in anime_data.items():
            for anime_schemas in value:
                status = self._update_anime(anime_schemas, key)
                id_list.append(anime_schemas.id)
                if not status:
                    write_list.append(self._create_schemas(
                        anime_schemas.id,
                        anime_schemas.link,
                        key
                    ))
        id_list_db = Anime.objects.filter(~Q(day_week=None)).\
            values_list('id_anime', flat=True)
        result_id = set(id_list_db) - set(id_list)
        if result_id:
            # Аниме которые закончили свой выход
            for id in result_id:
                Anime.objects.filter(id_anime=id).update(day_week=None)
        if write_list:
            return write_list

    def update_anime_anons(
        self,
        anime_data: List[schemas.AnimeFull]
    ) -> None | List[AnimeMini]:
        """Обновления данных anons"""
        write_list = []
        for anime_schemas in anime_data:
            status = self._update_anime(anime_schemas)
            if not status:
                write_list.append(self._create_schemas(
                    anime_schemas.id,
                    anime_schemas.link
                ))
        if write_list:
            return write_list

    def update_series(
        self,
        id: int,
        series_data: List[schemas.Series]
    ) -> None:
        """Обновления серий"""
        list_name_series = Series.objects.filter(id_anime=id).\
            values_list('name', flat=True)
        for data in series_data:
            if data.name not in list_name_series:
                Series.objects.create(
                    id_anime=id,
                    name=data.name,
                    serial=data.serial,
                    preview=data.preview,
                    number=get_number(data.name),
                    link=get_series_link(data.serial),
                )

    def update_indefinite_exit(
        self,
        anime_list: List[schemas.Anime]
    ) -> list | None:
        """Обновления аниме с неопределенным сроком выхода"""
        list_id_anime = Anime.objects.filter(indefinite_exit=False).\
            values_list('id_anime', flat=True)

        list_id_anime_indefinite = Anime.objects.\
            filter(indefinite_exit=True).values_list('id_anime', flat=True)

        # Список до записи
        write_list = []

        # Переворачиваем список с переданными аниме
        for anime in anime_list[::-1]:
            if anime.id in list_id_anime_indefinite:
                # обновить и перейти на следующую итерацию
                self._update_anime(anime)
                continue
            if anime.id not in list_id_anime:
                # добавить в список до записи
                write_list.append(anime)

        if write_list:
            return write_list
