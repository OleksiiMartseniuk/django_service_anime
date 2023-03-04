import logging

from rest_framework.exceptions import ValidationError

from django.db.models import Q
from django.shortcuts import get_object_or_404

from django_celery_beat.models import PeriodicTask

from src.anime.models import Anime

from . import task
from .telegram import TelegramApiClient
from ..models import BotUser, BotUserAnimePeriodTask


logger = logging.getLogger('db')


def write_id_images(anime: Anime, telegram_client: TelegramApiClient) -> None:
    """Запись id photo telegram в базу"""
    try:
        data = telegram_client.send_photo(anime.url_image_preview_s.path)
        id_photo = data['result']['photo'][-1]['file_id']
        anime.telegram_id_file = id_photo
        anime.save()
    except KeyError:
        logger.error(f'Нет ключа в словаре [{data}]')
    except Exception as ex:
        logger.error("Exception", exc_info=ex)


def formation_list_bot_user_anime_period_task(
    anime_objs: list[Anime], user: BotUser
) -> list[BotUserAnimePeriodTask]:
    """Формирования списка BotUserAnimePeriodTask"""
    result = []
    for anime in anime_objs:
        schedule = task.create_crontab_schedule(anime.timer)
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


def get_anime_tracked(user_id: int, subscriber: bool) -> list[Anime] | None:
    """Вывод аниме с отслеживание пользователя
    Parameters:
        subscriber (bool) - True: Получения список подписок
        subscriber (bool) - False: Получения список возможных подписок
    """
    user = get_object_or_404(BotUser, user_id=user_id)

    if subscriber:
        anime_list = user.track.all()
    else:
        anime_list_id = user.track.all().values_list('id', flat=True)
        anime_list = Anime.objects.filter(~Q(day_week=None) & ~Q(timer=0)).\
            exclude(id__in=anime_list_id).only('id', 'title', 'rating',
                                               'url_image_preview', 'votes',
                                               'timer', 'anons', 'link',
                                               'url_image_preview_s',
                                               'telegram_id_file', 'day_week')
    return anime_list


def update_user_tracked() -> None:
    """Обновить список подписок пользователя"""
    period_task_id_list = BotUserAnimePeriodTask.objects.filter(
        anime__timer=0
    ).values_list('period_task__id', flat=True)
    if period_task_id_list:
        PeriodicTask.objects.filter(id__in=period_task_id_list).delete()
    else:
        logger.info(
            'Нет данных для Обновить список подписок пользователя telegram'
        )
