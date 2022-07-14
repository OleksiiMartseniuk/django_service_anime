from typing import List

from rest_framework.exceptions import ValidationError

from src.anime.models import Anime, Series


WEEK = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


def get_anime_list_day(day: str) -> List[dict]:
    """Получения списка аниме по дню недели"""
    if day not in WEEK:
        raise ValidationError(f'Неверное значения[{day}]-[{", ".join(WEEK)}]')
    anime_list = Anime.objects. \
        filter(day_week=day). \
        values('id', 'title', 'url_image_preview')
    return anime_list


def get_series(id: int) -> List[Series]:
    """Получения серий"""
    pass
