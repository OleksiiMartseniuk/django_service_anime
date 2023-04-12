from django.db import models

from solo.models import SingletonModel
from django_celery_beat.models import PeriodicTask


class Genre(models.Model):
    """Жанры"""
    title = models.CharField('Названия', unique=True, max_length=30)

    def __str__(self):
        return self.title


class ScreenImages(models.Model):
    """Набор кадров"""
    images = models.ImageField(
        'Скрин [сервер]',
        upload_to='screen_images/',
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f"Images - {self.id}"


class Series(models.Model):
    """Серии"""
    id_anime = models.IntegerField('ID animevost')
    name = models.CharField('Названия', max_length=50)
    number = models.IntegerField('Номер серии', blank=True, null=True)
    serial = models.CharField(
        'Серийный номер',
        max_length=255,
        blank=True,
        null=True
    )
    preview = models.CharField(
        'Изображения предпросмотра',
        max_length=255,
        blank=True,
        null=True
    )
    link = models.CharField(
        'Ссылка на серию',
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Anime(models.Model):
    """Аниме"""
    id_anime = models.IntegerField('ID animevost', unique=True)
    title = models.CharField('Названия', max_length=255)
    link = models.CharField(
        'Ссылка animevost',
        max_length=255,
        blank=True,
        null=True
    )
    screen_image = models.ManyToManyField(
        ScreenImages,
        related_name='screen_images',
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='genres',
        blank=True
    )
    anime_composed = models.ManyToManyField(
        'Anime',
        related_name='anime_composeds',
        blank=True,
    )
    rating = models.IntegerField('Рейтинг')
    votes = models.IntegerField('Голоса')
    description = models.TextField('Описания')
    director = models.CharField(
        'Режиссёр',
        max_length=100,
        blank=True,
        null=True
    )
    url_image_preview = models.ImageField(
        'Preview изображения [сервер]',
        upload_to='preview/',
        blank=True,
        null=True
    )
    year = models.CharField('Год выпуска', max_length=20)
    timer = models.IntegerField('Время выхода серии', default=0)
    type = models.CharField('Тип', max_length=30)
    day_week = models.CharField(
        'День недели',
        max_length=20,
        default=None,
        blank=True,
        null=True
    )
    anons = models.BooleanField('Анонс', default=False)
    indefinite_exit = models.BooleanField(
        'Неопределенная дата выход',
        default=False
    )
    updated = models.DateTimeField('Обновлен', auto_now=True)

    def __str__(self):
        return self.title


class AnimeSettings(SingletonModel):
    status_task = models.BooleanField("Авто обновления", default=True)

    def set_status_task(self):
        task = PeriodicTask.objects.get(name='add-every-day-morning')
        task.enabled = self.status_task
        task.save(update_fields=["enabled"])

    def __str__(self):
        return "Anime Settings"
