from dataclasses import dataclass
import re
import logging
from typing import List

from src.anime.service.utils import get_number
from src.base.animevost import schemas
from src.anime.models import Anime, Series

from django.db.models import Q


logger = logging.getLogger('main')


@dataclass
class AnimeMini:
    """Мини описания аниме"""
    id: int
    link: str
    day: str = ''


class UpdateDataParser:
    """Обновления данных Parser"""
    def _create_schemas(self, id: int, link: str, day: str = '') -> AnimeMini:
        """Создать схему AnimeComposed"""
        return AnimeMini(id=id, link=link, day=day)

    def _update_anime(
            self,
            anime_data: schemas.AnimeData | schemas.Anime,
            day: str = ''
    ) -> bool:
        """Обновления данных anime"""
        anons = True if re.search(r'Анонс', anime_data.title) else False
        return Anime.objects.filter(id_anime=anime_data.id).update(
            title=anime_data.title,
            rating=anime_data.rating,
            votes=anime_data.votes,
            timer=anime_data.timer,
            day_week=day,
            anons=anons
        )

    def update_anime_schedule(
            self,
            anime_data: dict[str: List[schemas.AnimeFull]]
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
                    logger.info(f'Аниме(schedule) id={anime_schemas.id} '
                                f'записано')
        id_list_db = Anime.objects.filter(~Q(day_week=None)).\
            values_list('id_anime', flat=True)
        result_id = set(id_list_db) - set(id_list)
        if result_id:
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
                logger.info(f'Аниме(anons) id={anime_schemas.id} записано')
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
                    std=data.std,
                    hd=data.hd,
                    number=get_number(data.name)
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

        for anime in anime_list:
            if anime.id in list_id_anime_indefinite:
                # обновить и перейти на следующую итерацию
                self._update_anime(anime)
                continue
            if anime.id not in list_id_anime:
                # добавить в список до записи
                write_list.append(anime)

        if write_list:
            return write_list
