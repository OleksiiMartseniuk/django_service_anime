import logging
from typing import List

from django.db.models import Q

from src.base.animevost.service import ServiceAnimeVost
from src.base.animevost.service import ApiAnimeVostClient

from src.anime.service.write_db import WriteDB
from src.anime.service.update_db import UpdateDataParser, AnimeMini
from src.anime import models

from src.anime.service.utils import get_link


logger = logging.getLogger('main')


class ServiceAnime:
    def _write_anime(self, anime_list: List[AnimeMini]) -> None:
        """Запись дополнительных аниме"""
        if anime_list:
            for anime in anime_list:
                anime_she = ServiceAnimeVost().get_anime_data(
                    anime.id,
                    anime.link
                )
                WriteDB().write_anime_full(anime_she, anime.day)

    def anime_schedule(self) -> None:
        """Запись аниме расписания"""
        data_anime_parser = ServiceAnimeVost().get_data_anime_all(full=True)
        WriteDB().write_anime_schedule(data_anime_parser)
        logger.info('Запись аниме расписания')

    def anime_anons(self) -> None:
        """Запись аниме Анонс"""
        data_anime = ServiceAnimeVost().get_data_anime_anons_all(full=True)
        WriteDB().write_anime_anons(data_anime)
        logger.info('Запись аниме Анонс')

    def anime_schedule_update(self) -> None:
        """Обновления аниме расписания"""
        data_anime_parser = ServiceAnimeVost().get_data_anime_all()
        anime_list = UpdateDataParser().update_anime_schedule(
            data_anime_parser
        )
        self._write_anime(anime_list)
        logger.info('Обновления аниме расписания')

    def anime_anons_update(self) -> None:
        """Обновления аниме Анонс"""
        data_anime_parser = ServiceAnimeVost().get_data_anime_anons_all()
        anime_list = UpdateDataParser().update_anime_anons(
            data_anime_parser
        )
        self._write_anime(anime_list)
        logger.info('Обновления аниме Анонс')

    def delete_series(self):
        """Очистка данных таблицы Series"""
        models.Series.objects.all().delete()
        logger.info('Очистка данных таблицы Series')

    def series(self) -> None:
        """Запись серий"""
        list_id_anime = models.Anime.objects.values_list('id_anime', flat=True)
        for id in list_id_anime:
            data_series = ApiAnimeVostClient().get_play_list(id)
            WriteDB().write_series(id, data_series)
        logger.info('Запись серий')

    def series_update(self) -> None:
        """Обновления серий"""
        list_id_anime = models.Anime.objects.filter(~Q(day_week=None)).\
            values_list('id_anime', flat=True)
        for id in list_id_anime:
            data_series = ApiAnimeVostClient().get_play_list(id)
            UpdateDataParser().update_series(id, data_series)
        logger.info('Обновления серий')

    def update_indefinite_exit(self):
        """Обновления аниме с неопределенным сроком выхода"""
        data_anime = ApiAnimeVostClient().get_last_anime()
        write_list = UpdateDataParser().update_indefinite_exit(data_anime)
        logger.info('Обновления аниме с неопределенным сроком выхода')
        if write_list:
            for anime_shem in write_list:
                link = get_link(anime_shem.id, anime_shem.title)
                if not link:
                    # Если силка не сформирована преходит
                    # на следующую итерацию
                    logger.info(
                        f'Ссылка не сформирована anime[{anime_shem.title}]'
                    )
                    continue
                # формирования схемы AnimeFull
                anime_full = ServiceAnimeVost().get_anime_data(
                    anime_shem.id,
                    link
                )
                WriteDB().write_anime_full(anime_full, indefinite_exit=True)
                logger.info(
                    f'До запись anime в update_indefinite_exit '
                    f'[id_anime - {anime_full.id}, title - {anime_full.title}]'
                )
