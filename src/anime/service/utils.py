import re
import requests
import logging

from django.core.files import File
from django.db.models.fields.files import ImageFieldFile
from django.utils.text import slugify

from io import BytesIO


logger = logging.getLogger('db')


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
            logger.error("Скачивания изображения", exc_info=ex)
    logger.error(f'Неверный http статус [{responses.status_code}] '
                 f'url[{image_url}]')


def get_link(id_anime: int, title: str) -> str | None:
    """Формирования ссылки с названия"""
    base_url = 'https://animevost.org/tip/tv/' + f'{id_anime}-'
    title_list = re.split(r'/ |\[', title)
    if len(title_list) > 1:
        slug = slugify(title_list[1])
        return base_url + slug + '.html'
    else:
        logger.error(
            f'Неверный формат в названии - [{title}] ссылка не сформирована'
        )


def get_series_link(serial: str) -> str:
    """Получения силки на серию"""
    return f'https://animevost.org/frame5.php?play={serial}&old=1'
