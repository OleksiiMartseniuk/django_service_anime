import json

from datetime import datetime

from django_celery_beat.models import CrontabSchedule, PeriodicTask

from src.anime.models import Anime


def create_crontab_schedule(time: int, day: str) -> CrontabSchedule:
    """Создания кроны"""
    # 1663277581
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
