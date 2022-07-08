from src.base.animevost.service import ServiceAnimeVost
from src.anime.service.write_db import WriteDB
from src.anime.service.update_db import UpdateDataParser
from src.anime import models


class ServiceAnime:
    def anime_schedule(self) -> None:
        """Запись аниме расписания"""
        data_anime_parser = ServiceAnimeVost().get_data_anime_all(full=True)
        WriteDB().write_anime_schedule(data_anime_parser)

    def anime_anons(self) -> None:
        """Запись аниме Анонс"""
        data_anime = ServiceAnimeVost().get_data_anime_anons_all(full=True)
        WriteDB().write_anime_anons(data_anime)

    def anime_schedule_update(self) -> None:
        """Обновления аниме расписания"""
        data_anime_parser = ServiceAnimeVost().get_data_anime_all()
        anime_list = UpdateDataParser().update_anime_schedule(data_anime_parser)
        if anime_list:
            for anime in anime_list:
                ServiceAnimeVost().get_anime_data(anime.id_anime, anime.link)



    def anime_anons_update(self) -> None:
        """Обновления аниме Анонс"""
        pass

    def delete_table(self) -> None:
        """Очистка данных таблиц и кеша-жанров"""
        WriteDB().clear_cash_memory()
        models.Anime.objects.all().delete()
        models.ScreenImages.objects.all().delete()
        models.Genre.objects.all().delete()
