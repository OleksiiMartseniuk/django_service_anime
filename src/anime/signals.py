from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import AnimeSettings


@receiver(pre_save, sender=AnimeSettings)
def save_task_status(sender, instance: AnimeSettings, **kwargs):
    current = instance
    previous = AnimeSettings.get_solo()
    if current.status_task != previous.status_task:
        current.set_status_task()