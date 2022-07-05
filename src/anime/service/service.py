from src.base.animevost.service import ServiceAnimeVost
from src.anime.service.write_db import WriteDB
from src.anime import models


class ServiceAnime:
    def anime_schedule(self):
        """Запись аниме расписания"""
        data_anime_parser = ServiceAnimeVost().get_data_anime_all(full=True)
        WriteDB().write_anime_schedule(data_anime_parser)

    def anime_anons(self):
        """Запись аниме Анонс"""
        data_anime = ServiceAnimeVost().get_data_anime_anons_all(full=True)
        WriteDB().write_anime_anons(data_anime)

    def delete_table(self):
        """Очистка данных таблиц и кеша-жанров"""
        WriteDB().clear_cash_memory()
        models.Anime.objects.all().delete()
        models.ScreenImages.objects.all().delete()
        models.Genre.objects.all().delete()
