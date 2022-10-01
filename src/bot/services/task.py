import json
import logging

from datetime import datetime
from dataclasses import dataclass

from rest_framework.exceptions import ValidationError
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from src.bot.models import BotUser


logger = logging.getLogger('main')


@dataclass
class PeriodicTaskObj:
    task: PeriodicTask
    create: bool


def create_crontab_schedule(time: int) -> CrontabSchedule:
    """Создания кроны"""
    if not time:
        logger.error('Время выхода серий отсутствует')
        raise ValidationError('Время выхода серий отсутствует')

    date = datetime.fromtimestamp(time)
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=date.minute,
        hour=date.hour,
        day_of_week=date.weekday()
    )
    return schedule


def create_periodic_task(
    anime_id: int, schedule: CrontabSchedule, user: BotUser
) -> PeriodicTaskObj:
    """Создания задачи с отслеживанием аниме"""
    periodic_task, create = PeriodicTask.objects.get_or_create(
        crontab=schedule,
        name=f'{anime_id}_{user.id}',
        task='src.bot.tasks.reminders',
        args=json.dumps([user.chat_id, anime_id]),
    )
    return PeriodicTaskObj(periodic_task, create)
