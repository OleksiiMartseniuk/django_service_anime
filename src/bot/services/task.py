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


def create_crontab_schedule(time: int, day: str) -> CrontabSchedule:
    """Создания кроны"""
    # TODO поверить формирования времени
    if not day:
        logger.error('Названия дня недели отсутствует')
        raise ValidationError('Названия дня недели отсутствует')
    if time:
        date = datetime.fromtimestamp(time)
        hour = date.hour
        minute = date.minute
    else:
        # Default значения времени
        hour = 10
        minute = 0
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=str(minute),
        hour=str(hour),
        day_of_week=day
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
