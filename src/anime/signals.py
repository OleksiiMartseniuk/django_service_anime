from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from .models import AnimeSettings, ScreenImages, Anime


@receiver(pre_save, sender=AnimeSettings)
def save_task_status(sender, instance: AnimeSettings, **kwargs):
    # The first run of the object model does not contain AnimeSettings
    if AnimeSettings.objects.all().count():
        current = instance
        previous = AnimeSettings.get_solo()
        if current.status_task != previous.status_task:
            current.set_status_task()


@receiver(post_delete, sender=Anime)
@receiver(post_delete, sender=ScreenImages)
def save_task_status(sender, instance: ScreenImages | Anime, **kwargs):
    if instance.pk is None:
        return False

    if isinstance(instance, ScreenImages):
        if instance.images:
            instance.images.delete(save=False)

    if isinstance(instance, Anime):
        if instance.url_image_preview:
            instance.url_image_preview.delete(save=False)
