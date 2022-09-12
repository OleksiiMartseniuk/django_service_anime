import logging

from rest_framework.exceptions import ValidationError

from src.anime.models import Anime

from .telegram import TelegramApiClient
from ..models import BotUser

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


def add_anime(anime_ids: list[int], user_id: int) -> None:
    """Добавить аниме в отслеживаемые"""
    if Anime.objects.filter(id__in=anime_ids).exists():
        anime_objs = Anime.objects.filter(id__in=anime_ids)
    else:
        logger.debug('Аниме не найдено')
        raise ValidationError('Аниме не найдено', code=404)

    if BotUser.objects.filter(user_id=user_id).exists():
        user = BotUser.objects.get(user_id=user_id)
        user.anime.add(*anime_objs)
    else:
        logger.debug('Пользователь не найде')
        raise ValidationError('Пользователь не найде', code=404)
