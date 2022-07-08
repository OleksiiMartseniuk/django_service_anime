from dataclasses import dataclass
import re
import logging
from typing import List

from src.base.animevost import schemas
from src.anime.models import Anime


logger = logging.getLogger(__name__)


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
        return AnimeMini(
            id=id,
            link=link,
            day=day
        )

    def _update_anime(
            self,
            anime_data: schemas.AnimeData,
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
        write_list = []
        for key, value in anime_data.items():
            for anime_schemas in value:
                status = self._update_anime(anime_schemas, key)
                if not status:
                    write_list.append(self._create_schemas(
                        anime_schemas.id,
                        anime_schemas.link,
                        key
                    ))
                    logger.info(f'Аниме(schedule) id={anime_schemas.id} '
                                f'записано')
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
