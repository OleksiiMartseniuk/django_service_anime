from django.db import models

from src.anime.choices import WeekDayChoices


class AnimeVost(models.Model):
    anime_id = models.IntegerField(unique=True)
    title_ru = models.CharField(
        max_length=255,
        blank=True,
    )
    title_en = models.CharField(
        max_length=255,
        blank=True,
    )
    screen_image = models.ManyToManyField(
        "ScreenImagesAnimeVost",
        related_name="animevost",
        blank=True,
    )
    genre = models.ManyToManyField(
        "Genre",
        related_name="animevost",
        blank=True
    )
    anime_composed = models.ManyToManyField(
        "AnimeVost",
        blank=True,
    )
    series = models.ManyToManyField(
        "SeriesAnimeVost",
        blank=True,
        related_name="animevost"
    )
    rating = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    director = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    url_image_preview = models.ImageField(
        upload_to="preview/",
        blank=True,
        null=True
    )
    year = models.CharField(
        max_length=20,
        blank=True,
    )
    timer = models.IntegerField(default=0)
    type = models.CharField(
        max_length=30,
        blank=True,
    )
    day_week = models.IntegerField(
        choices=WeekDayChoices.choices,
        default=None,
        blank=True,
        null=True,
    )
    anons = models.BooleanField(default=False)
    anons_date = models.DateField(
        blank=True,
        null=True,
    )
    indefinite_exit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.id}] {self.title_en}"
