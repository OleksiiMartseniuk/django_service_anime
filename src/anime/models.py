from django.db import models
from django.conf import settings

from .service.admin import messages


class Genre(models.Model):
    """Жанры"""
    title = models.CharField('Названия', unique=True, max_length=30)

    def __str__(self):
        return self.title


class ScreenImages(models.Model):
    """Набор кадров"""
    images = models.CharField('Скрин', max_length=255)
    images_s = models.ImageField(
        'Скрин [сервер]',
        upload_to='screen_images/',
        blank=True,
        null=True
    )


class Series(models.Model):
    """Серии"""
    id_anime = models.IntegerField('ID animevost')
    name = models.CharField('Названия', max_length=50)
    std = models.CharField('sd качество', max_length=255)
    hd = models.CharField('hd качество', max_length=255)
    number = models.IntegerField('Номер серии', blank=True, null=True)

    def __str__(self):
        return self.name


class Anime(models.Model):
    """Аниме"""
    id_anime = models.IntegerField('ID animevost', unique=True)
    title = models.CharField('Названия', max_length=255)
    link = models.CharField('Ссылка animevost', max_length=255)
    screen_image = models.ManyToManyField(
        ScreenImages,
        related_name='screen_images',
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='genres'
    )
    anime_composed = models.ManyToManyField(
        'Anime',
        related_name='anime_composeds',
        blank=True,
    )
    rating = models.IntegerField('Рейтинг')
    votes = models.IntegerField('Голоса')
    description = models.TextField('Описания')
    director = models.CharField('Режиссёр', max_length=100)
    url_image_preview = models.CharField('Preview изображения', max_length=255)
    url_image_preview_s = models.ImageField(
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
        default='',
        blank=True
    )
    anons = models.BooleanField('Анонс', default=False)

    class Meta:
        # add index id_anime
        pass

    def __str__(self):
        return self.title


class Statistics(models.Model):
    """Статистика роботы Parser"""
    MESSAGE_CHOICES = [
        ('schedule', messages.SCHEDULE_FORM),
        ('anons', messages.ANONS_FORM),
        ('delete', messages.DElETE_SCHEDULE_FORM),
        ('schedule_update', messages.SCHEDULE_UPDATE_FORM),
        ('anons_update', messages.ANONS_UPDATE_FORM),
        ('series', messages.SERIES_FORM),
        ('series_update', messages.SERIES_UPDATE_FORM),
        ('delete_series', messages.DElETE_SERIES_FORM),
    ]
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='statistics',
        on_delete=models.CASCADE,
    )
    message = models.CharField(max_length=16, choices=MESSAGE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
