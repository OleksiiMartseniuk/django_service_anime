import json
import logging

from datetime import datetime

from rest_framework.exceptions import ValidationError
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from src.bot.models import BotUser


logger = logging.getLogger('main')


def create_crontab_schedule(time: int, day: str) -> CrontabSchedule:
    """Создания кроны"""
    if not day:
        logger.error('Названия дня недели отсутствует')
        raise ValidationError('Названия дня недели отсутствует')
    if time:
        date = datetime.utcfromtimestamp(time)
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
) -> PeriodicTask:
    """Создания задачи с отслеживанием аниме"""
    return PeriodicTask.objects.create(
        crontab=schedule,
        name=f'{anime_id}_{user.id}',
        task='src.bot.tasks.reminders',
        args=json.dumps([user.chat_id, anime_id]),
    )
