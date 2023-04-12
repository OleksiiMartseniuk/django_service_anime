from .api import ApiAnimeVostClient
from .parser import ParserClient
from .schemas import AnimeData, AnimeFull, AnimeMin, Anime, Series
from .utils import exception_check


class ServiceAnimeVost:

    def _create_anime_full_list(
            self,
            anime_min_list: list[AnimeMin]
    ) -> list[AnimeFull | None]:
        """Создания списка схемы AnimeFull"""
        list_anime = []
        for anime in anime_min_list:
            anime_full = self.get_anime(anime)
            if anime_full:
                list_anime.append(anime_full)
        return list_anime

    @exception_check
    def get_anime(self, anime: AnimeMin) -> AnimeFull | None:
        """Get schemas AnimeFull"""
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
    ) -> dict[str, list[AnimeFull]] | dict:
        anime_week = {}
        data_parser = ParserClient().get_schedule(full)
        for key, value in data_parser.items():
            if value:
                anime_week[key] = self._create_anime_full_list(value)
        return anime_week

    def get_data_anime_anons_all(
            self,
            full: bool = False
    ) -> list[AnimeFull | None] | None:
        data_parser = ParserClient().get_anons(full)
        if data_parser:
            return self._create_anime_full_list(data_parser)

    def get_anime_data(self, id: int, link: str) -> AnimeFull | None:
        """Get one anime"""
        data = ParserClient().get_anime_one(id, link)
        return self.get_anime(data)

    @exception_check
    def get_list_series(self, anime_id: int) -> list[Series] | None:
        return ApiAnimeVostClient().get_play_list(id=anime_id)

    @exception_check
    def get_anime_indefinite_exit(
        self,
        page: int = 1,
        quantity: int = 30
    ) -> list[Anime] | None:
        return ApiAnimeVostClient().get_last_anime(
            page=page,
            quantity=quantity,
        )
