from django.db import models
from django.conf import settings


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
        default=None,
        blank=True,
        null=True
    )
    anons = models.BooleanField('Анонс', default=False)
    indefinite_exit = models.BooleanField(
        'Неопределенный выход',
        default=False
    )

    def __str__(self):
        return self.title


class Statistics(models.Model):
    """Статистика роботы Parser"""
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='statistics',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    message = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


class BotStatistics(models.Model):
    """Статистика бота"""
    id_user = models.IntegerField('id пользователя')
    action = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created = models.DateTimeField()

    def __str__(self):
        return f'Пользователь [{self.id_user}] действия [{self.action}]'


class BotCollBackMessage(models.Model):
    """Сообщения пользователя"""
    id_user = models.IntegerField('id пользователя')
    message = models.TextField()
    read = models.BooleanField('Прочитано', default=False)
    created = models.DateTimeField()

    def __str__(self):
        return f'Пользователь [{self.id_user}]'
