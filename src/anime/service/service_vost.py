import logging
import time
from typing import List

from django.db.models import Q

from src.base.animevost.service import ServiceAnimeVost

from src.anime.service.write_db import WriteDB
from src.anime.service.update_db import UpdateDataParser, AnimeMini
from src.anime import models

from src.anime.service.utils import get_link


logger = logging.getLogger('db')


class ServiceAnime:
    def _write_anime(self, anime_list: List[AnimeMini]) -> None:
        """Запись дополнительных аниме"""
        if anime_list:
            for anime in anime_list:
                anime_she = ServiceAnimeVost().get_anime_data(
                    anime.id,
                    anime.link
                )
                if anime_she:
                    WriteDB().write_anime_full(anime_she, anime.day)
                else:
                    logger.error(
                        "Anime with id_animevost [%s] not found",
                        anime.id
                    )

    def anime_schedule(self) -> None:
        """Запись аниме расписания"""
        logger.info('Запись аниме расписания запущено.')
        start_time = time.time()
        data_anime_parser = ServiceAnimeVost().get_data_anime_all(full=True)
        if data_anime_parser:
            WriteDB().write_anime_schedule(data_anime_parser)
        else:
            logger.error("Data for writing anime_schedule not")
        finish = time.time() - start_time
        logger.info(f'Запись аниме расписания завершена. Время [{finish}]')

    def anime_anons(self) -> None:
        """Запись аниме Анонс"""
        logger.info('Запись аниме Анонс запущено.')
        start_time = time.time()
        data_anime = ServiceAnimeVost().get_data_anime_anons_all(full=True)
        if data_anime and len(data_anime):
            WriteDB().write_anime_anons(data_anime)
        else:
            logger.error("Data for writing anime_anons not")
        finish = time.time() - start_time
        logger.info(f'Запись аниме Анонс завершена. Время [{finish}]')

    def anime_schedule_update(self) -> None:
        """Обновления аниме расписания"""
        logger.info('Обновления аниме расписания запущено.')
        start_time = time.time()
        data_anime_parser = ServiceAnimeVost().get_data_anime_all()
        if data_anime_parser:
            anime_list = UpdateDataParser().update_anime_schedule(
                data_anime_parser
            )
            if anime_list:
                self._write_anime(anime_list)
        finish = time.time() - start_time
        logger.info(f'Обновления аниме расписания завершена. Время [{finish}]')

    def anime_anons_update(self) -> None:
        """Обновления аниме Анонс"""
        logger.info('Обновления аниме Анонс запущено.')
        start_time = time.time()
        data_anime_parser = ServiceAnimeVost().get_data_anime_anons_all()
        if data_anime_parser:
            anime_list = UpdateDataParser().update_anime_anons(
                data_anime_parser
            )
            if anime_list:
                self._write_anime(anime_list)
        finish = time.time() - start_time
        logger.info(f'Обновления аниме Анонс завершено. Время [{finish}]')

    def series(self) -> None:
        """Запись серий"""
        logger.info('Запись серий запущено.')
        start_time = time.time()
        list_id_anime = models.Anime.objects.values_list('id_anime', flat=True)
        for id in list_id_anime:
            data_series = ServiceAnimeVost().get_list_series(id)
            if data_series:
                WriteDB().write_series(id, data_series)
            else:
                logger.error(f"Data write series not. id_animevost[{id}]")
        finish = time.time() - start_time
        logger.info(f'Запись серий завершена. Время [{finish}]')

    def series_update(self) -> None:
        """Обновления серий"""
        logger.info('Обновления серий запущено.')
        start_time = time.time()
        list_id_anime = models.Anime.objects.filter(~Q(day_week=None)).\
            values_list('id_anime', flat=True)
        for id in list_id_anime:
            data_series = ServiceAnimeVost().get_list_series(id)
            if data_series:
                UpdateDataParser().update_series(id, data_series)
            else:
                logger.error(f"Data write series not. id_animevost[{id}]")
        finish = time.time() - start_time
        logger.info(f'Обновления серий завершено. Время [{finish}]')

    def update_indefinite_exit(self):
        """Обновления аниме с неопределенным сроком выхода"""
        logger.info(
            'Обновления аниме с неопределенным сроком выхода. '
            'Сбор данных начат'
        )
        start_time = time.time()
        data_anime = ServiceAnimeVost().get_anime_indefinite_exit()
        if data_anime:
            write_list = UpdateDataParser().update_indefinite_exit(data_anime)
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
                    if anime_full:
                        WriteDB().write_anime_full(
                            anime_data=anime_full,
                            indefinite_exit=True
                        )
                    else:
                        logger.error(
                            "Not data for write id_animevost [%s]",
                            anime_shem.id
                        )
        else:
            logger.error(
                "Not data update update_indefinite_exit ServiceAnimeVost"
            )
        finish = time.time() - start_time
        logger.info(
            'Обновления аниме с неопределенным сроком выхода. '
            'Завершено время [%s]',
            finish
        )
