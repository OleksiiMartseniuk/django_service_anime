import logging

from rest_framework.exceptions import ValidationError
from django_celery_beat.models import PeriodicTask

from src.anime.models import Anime

from . import task
from .telegram import TelegramApiClient
from ..models import BotUser, BotUserAnimePeriodTask


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


def formation_list_bot_user_anime_period_task(
    anime_objs: list[Anime], user: BotUser
) -> list[BotUserAnimePeriodTask]:
    """Формирования списка BotUserAnimePeriodTask"""
    result = []
    for anime in anime_objs:
        schedule = task.create_crontab_schedule(anime.timer, anime.day_week)
        task_obj = task.create_periodic_task(anime.id, schedule, user)

        # Проверка на уникальность
        if not task_obj.create:
            logger.error(f'Запись существует anime[{anime.id}] user[{user.id}]'
                         f'period_task[{task_obj.task.id}]')
            continue

        result.append(
            BotUserAnimePeriodTask(
                user=user, anime=anime, period_task=task_obj.task
            )
        )
    return result


def add_anime(anime_ids: list[int], user_id: int) -> None:
    """Добавить аниме в отслеживаемые"""
    if Anime.objects.filter(id__in=anime_ids).exists():
        anime_objs = Anime.objects.filter(id__in=anime_ids)
    else:
        logger.error(f'Аниме не найдено [{anime_ids}]')
        raise ValidationError('Аниме не найдено', code=404)

    if BotUser.objects.filter(user_id=user_id).exists():
        user = BotUser.objects.get(user_id=user_id)
        BotUserAnimePeriodTask.objects.bulk_create(
            formation_list_bot_user_anime_period_task(anime_objs, user)
        )
    else:
        logger.error(f'Пользователь не найде [{user_id}]')
        raise ValidationError('Пользователь не найде', code=404)


def delate_anime(anime_ids: list[int], user_id: int) -> None:
    """Удалить аниме с отслеживание"""
    period_task_id_list = BotUserAnimePeriodTask.objects.filter(
        anime__id__in=anime_ids,
        user__user_id=user_id
    ).values_list('period_task__id', flat=True)

    if not period_task_id_list:
        logger.warning(f'Не найдено ни одного объекта '
                       f'BotUserAnimePeriodTask anime_ids[{anime_ids}] '
                       f'user_id[{user_id}]')
        raise ValidationError(
            'Не найдено ни одного объекта BotUserAnimePeriodTask',
            code=404
        )
    # Удаления PeriodicTask и также удаляйте объекты,
    # которые имеют ссылки на него (BotUserAnimePeriodTask)
    PeriodicTask.objects.filter(id__in=period_task_id_list).delete()
