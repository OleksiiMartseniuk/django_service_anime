import logging

from src.bot.models import BotIdImage

from .telegram import TelegramApiClient

logger = logging.getLogger('main')


def write_id_images(id_anime: int, path_img: str) -> None:
    """Запись id photo telegram в базу"""
    data = TelegramApiClient().send_photo(path_img)
    if data:
        try:
            id_photo = data['result']['photo'][-1]['file_id']
            BotIdImage.objects.create(id_photo=id_photo, id_anime=id_anime)
        except KeyError:
            logger.error(f'Нет ключа в словаре [{data}]')
        except Exception as ex:
            logger.error(ex)
    else:
        logger.info('Нет данных в переменой data')
