from .api import ApiAnimeVostClient
from .parser import ParserClient
from .schemas import AnimeData, AnimeFull, AnimeMin


class ServiceAnimeVost:
    def _create_anime_full_list(
            self,
            list_anime_shem: list[AnimeMin]
    ) -> list[AnimeFull]:
        """Создания списка схемы AnimeFull"""
        list_anime = []
        for anime in list_anime_shem:
            list_anime.append(self.get_anime(anime))
        return list_anime

    def get_anime(self, anime: AnimeMin) -> AnimeFull:
        """Создания схему AnimeFull"""
        anime_schem = ApiAnimeVostClient().get_anime(anime.id_anime)
        anime_link = anime.link
        list_anime_composed = []
        if anime.anime_composed:
            # Получения данных с api 'аниме состоит'
            for anime_min in anime.anime_composed:
                anime_composed_api = ApiAnimeVostClient().get_anime(
                    anime_min.id_anime
                )
                anime_composed_link = anime_min.link
                anime_data_composed = AnimeData(
                    **anime_composed_api.dict(),
                    link=anime_composed_link
                )
                list_anime_composed.append(anime_data_composed)
        anime_data = AnimeFull(
            **anime_schem.dict(),
            link=anime_link,
            anime_composed=list_anime_composed
        )
        return anime_data

    def get_data_anime_all(
            self,
            full: bool = False
    ) -> dict[str: list[AnimeFull]]:
        """
        Получения данных аниме
        :arg full: флаг для полного или частичного сбора данных
        Полный сбор ~72с
        Частичный сбор ~15с
        """
        anime_week = {}
        # Получения данных парсера
        data_parser = ParserClient().get_schedule(full)
        for key, value in data_parser.items():
            anime_week[key] = self._create_anime_full_list(value)
        return anime_week

    def get_data_anime_anons_all(
            self,
            full: bool = False
    ) -> list[AnimeFull]:
        """
        Получения данных аниме Anons
        :arg full: флаг для полного или частичного сбора данных
        Полный сбор ~28с
        Частичный сбор ~8c
        """
        data_parser = ParserClient().get_anons(full)
        return self._create_anime_full_list(data_parser)

    def get_anime_data(self, id: int, link: str) -> AnimeFull:
        """Создания схему AnimeFull через аргументы"""
        data = ParserClient().get_anime_one(id, link)
        return self.get_anime(data)
