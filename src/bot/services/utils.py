import logging

from src.anime.models import Anime

from .telegram import TelegramApiClient

logger = logging.getLogger('main')


def write_id_images(anime: Anime) -> None:
    """Запись id photo telegram в базу"""
    data = TelegramApiClient().send_photo(anime.url_image_preview_s.path)
    if data:
        try:
            id_photo = data['result']['photo'][-1]['file_id']
            anime.telegram_id_file = id_photo
            anime.save()
        except KeyError:
            logger.error(f'Нет ключа в словаре [{data}]')
        except Exception as ex:
            logger.error(ex)
    else:
        logger.error(f'Нет данных в переменой data [{anime.title}]')
