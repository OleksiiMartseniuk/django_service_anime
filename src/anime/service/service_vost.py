import logging
from typing import List

from django.db.models import Q

from src.base.animevost.service import ServiceAnimeVost
from src.base.animevost.service import ApiAnimeVostClient
from src.anime.service.write_db import WriteDB
from src.anime.service.update_db import UpdateDataParser, AnimeMini
from src.anime import models


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

    def delete_table(self) -> None:
        """Очистка данных таблиц и кеша-жанров"""
        models.Anime.objects.all().delete()
        models.ScreenImages.objects.all().delete()
        models.Genre.objects.all().delete()
        logger.info('Очистка данных таблиц и кеша-жанров')

    def series(self) -> None:
        """Запись серий"""
        list_id_anime = models.Anime.objects.values_list('id_anime', flat=True)
        for id in list_id_anime:
            data_series = ApiAnimeVostClient().get_play_list(id)
            WriteDB().write_series(id, data_series)
        logger.info('Запись серий')

    def series_update(self) -> None:
        """Обновления серий"""
        list_id_anime = models.Anime.objects.filter(~Q(day_week='')).\
            values_list('id_anime', flat=True)
        for id in list_id_anime:
            data_series = ApiAnimeVostClient().get_play_list(id)
            UpdateDataParser().update_series(id, data_series)
        logger.info('Обновления серий')
        