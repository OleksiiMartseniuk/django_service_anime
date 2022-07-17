import requests
import logging

from typing import List
from io import BytesIO

from rest_framework.exceptions import ValidationError

from django.core.files import File
from django.db.models.fields.files import ImageFieldFile

from src.anime.models import Anime


logger = logging.getLogger('main')
WEEK = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


def get_anime_list_day(day: str) -> List[dict]:
    """Получения списка аниме по дню недели"""
    if day not in WEEK:
        raise ValidationError(f'Неверное значения[{day}]-[{", ".join(WEEK)}]')
    anime_list = Anime.objects. \
        filter(day_week=day). \
        values('id', 'title', 'url_image_preview', 'timer')
    return anime_list


def download_image(obj_image: ImageFieldFile, image_url: str) -> None:
    """Скачивания изображений"""
    responses = requests.get(image_url)
    if responses.status_code == 200:
        try:
            fp = BytesIO()
            fp.write(responses.content)
            file_name = image_url.split("/")[-1]
            obj_image.save(file_name, File(fp))
            return None
        except Exception as ex:
            logger.error(str(ex))
    logger.error(f'Неверный http статус [{responses.status_code}] '
                 f'url[{image_url}]')
