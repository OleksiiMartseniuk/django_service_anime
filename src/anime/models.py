from django.db import models


class Genre(models.Model):
    """Жанры"""
    title = models.CharField('Названия', unique=True, max_length=30)

    def __str__(self):
        return self.title


class ScreenImages(models.Model):
    """Набор кадров"""
    images = models.CharField('Скрин', max_length=255)


class Series(models.Model):
    """Серии"""
    name = models.CharField('Номер серии', max_length=50)
    std = models.CharField('sd качество', max_length=255)
    hd = models.CharField('hd качество', max_length=255)

    def __str__(self):
        return self.name


class Anime(models.Model):
    """Аниме"""
    id_anime = models.IntegerField('ID animevost', unique=True)
    title = models.CharField('Названия', max_length=255)
    link = models.CharField('Ссылка animevost', max_length=255)
    screen_image = models.ManyToManyField(
        ScreenImages,
        related_name='screen_images'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='genres'
    )
    rating = models.IntegerField('Рейтинг')
    votes = models.IntegerField('Голоса')
    description = models.TextField('Описания')
    director = models.CharField('Режиссёр', max_length=100)
    url_image_preview = models.CharField('Preview изображения', max_length=255)
    year = models.CharField('Год выпуска', max_length=20)
    timer = models.IntegerField('Время выхода серии', default=0)
    type = models.CharField('Тип', max_length=10)
    day_week = models.CharField('День недели', max_length=20, default='')
    anons = models.BooleanField('Анонс', default=False)

    class Meta:
        # add index id_anime
        pass

    def __str__(self):
        return self.title
