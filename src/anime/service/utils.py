import re
import requests
import logging
import os
import glob

from django.core.files import File
from django.db.models.fields.files import ImageFieldFile
from django.conf import settings

from io import BytesIO


logger = logging.getLogger('main')


def get_number(name: str) -> int | None:
    """Получение номера серии"""
    number = re.search(r'^\d*', name).group()
    return int(number) if number else None


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


def delete_img_files() -> None:
    """Удаления всех изображений с директории"""
    path_list = [
        f'{settings.MEDIA_ROOT}/preview/*',
        f'{settings.MEDIA_ROOT}/screen_images/*'
    ]
    for path in path_list:
        for file in glob.glob(path):
            os.remove(file)
