import logging
from datetime import datetime

from django.db import transaction
from django.utils.timezone import make_aware

from src.anime.models import (
    AniLibria,
    ScreenImages,
    Genre,
    StatusChoices,
    AnimeTypeChoices,
    SeasonChoices,
    WeekDayChoices,
    PosterChoices,
)
from src.anime.utils import download_image
from src.utils.ani_libria.api import ClientAniLibria
from src.utils.ani_libria.exception import RequestErrorAniLibria
from src.utils.ani_libria.schemas import Title, Posters


logger = logging.getLogger("db")


class AniLibriaSync:
    def __init__(self):
        self.api_ani_libria_client = ClientAniLibria()
        self.base_view_url = "https://www.anilibria.tv"

    def sync(self) -> None:
        self.sync_schedule()

    def sync_schedule(self) -> None:
        try:
            anime_data_schedule = self.api_ani_libria_client.get_schedule()
        except RequestErrorAniLibria as ex:
            logger.error("No data, anime schedule", exc_info=ex)
            return None
        for schedule in anime_data_schedule.schedule:
            for anime in schedule.list:
                if AniLibria.objects.filter(anime_id=anime.id).exists():
                    # update
                    pass
                else:
                    try:
                        self.create_anime(anime_schema=anime)
                    except Exception as ex:
                        logger.error(
                            f"AniLibria don't created {anime.names.en}",
                            exc_info=ex,
                        )

    # come up with another way
    # @transaction.atomic
    def create_anime(self, anime_schema: Title) -> None:
        with transaction.atomic():
            data_dict = self.__get_dict_anilibria(anime=anime_schema)
            anime = AniLibria.objects.create(**data_dict)
            self.__create_genres(anime=anime, genres=anime_schema.genres)

        self.__create_screen_images(anime=anime, posters=anime_schema.posters)
        # add series
        # add anime_composed

    def update_anime(self, anime_schema: Title) -> None:
        # need update images
        pass

    @staticmethod
    def __get_dict_anilibria(anime: Title) -> dict:
        anime_dict = {
            "anime_id": anime.id,
            "code": anime.code,
            "name_ru": anime.names.ru,
            "name_en": anime.names.en,
            "name_alternative": anime.names.alternative,
            "announce": anime.announce,
            "status": StatusChoices(anime.status.code),
            "updated": make_aware(datetime.fromtimestamp(anime.updated)),
            "last_change": make_aware(
                datetime.fromtimestamp(anime.last_change)
            ),
            "anime_type": AnimeTypeChoices(anime.type.code),
            "season": SeasonChoices(anime.season.code),
            "description": anime.description,
            "in_favorites": anime.in_favorites,
            "blocked": anime.blocked.blocked,
            "bakanim": anime.blocked.bakanim,
        }
        if anime.season.week_day:
            anime_dict["week_day"] = WeekDayChoices(anime.season.week_day)
        return anime_dict

    def __create_screen_images(
        self,
        anime: AniLibria,
        posters: Posters,
    ) -> None:
        for key, poster in posters.dict().items():
            obj = ScreenImages.objects.create(
                anilibria=anime,
                poster=PosterChoices(key),
            )
            is_download_image = download_image(
                obj_image=obj.images,
                image_url=f"{self.base_view_url}{poster['url']}",
            )
            if not is_download_image:
                obj.delete()

    @staticmethod
    def __create_genres(anime: AniLibria, genres: list[str]) -> None:
        for genre in genres:
            genre, _ = Genre.objects.get_or_create(title=genre.lower())
            anime.genres.add(genre)

    @staticmethod
    def __create_series() -> None:
        pass
