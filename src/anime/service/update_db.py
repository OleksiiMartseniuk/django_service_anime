import re
import logging
from typing import List

from src.base.animevost import schemas
from src.anime.models import Anime
from src.anime.service.write_db import WriteDB


logger = logging.getLogger(__name__)


class UpdateDataParser:
    """Обновления данных Parser"""
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
    ) -> None:
        """Обновления данных schedule"""
        for key, value in anime_data.items():
            for anime_schemas in value:
                status = self._update_anime(anime_schemas, key)
                if not status:
                    WriteDB().write_anime_full(anime_schemas, key)
                    logger.info(f'Аниме(schedule) id={anime_schemas.id} '
                                f'записано')

    def update_anime_anons(self, anime_data: List[schemas.AnimeFull]) -> None:
        """Обновления данных anons"""
        for anime_schemas in anime_data:
            status = self._update_anime(anime_schemas)
            if not status:
                WriteDB().write_anime_full(anime_schemas)
                logger.info(f'Аниме(anons) id={anime_schemas.id} записано')
