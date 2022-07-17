import logging

from typing import List

from rest_framework.exceptions import ValidationError

from src.anime.models import Anime


WEEK = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


def get_anime_list_day(day: str) -> List[dict]:
    """Получения списка аниме по дню недели"""
    if day not in WEEK:
        raise ValidationError(f'Неверное значения[{day}]-[{", ".join(WEEK)}]')
    anime_list = Anime.objects.filter(day_week=day). \
        only('id', 'title', 'url_image_preview',
             'url_image_preview_s', 'timer')
    return anime_list
