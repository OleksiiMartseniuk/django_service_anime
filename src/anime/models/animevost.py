from django.db import models


class AnimeVost(models.Model):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    WEEK_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )

    id_anime = models.IntegerField(unique=True)
    title_ru = models.CharField(
        max_length=255,
        blank=True,
    )
    title_en = models.CharField(
        max_length=255,
        blank=True,
    )
    screen_image = models.ManyToManyField(
        'ScreenImages',
        related_name='screen_images',
        blank=True,
    )
    genre = models.ManyToManyField(
        'Genre',
        related_name='genres',
        blank=True
    )
    anime_composed = models.ManyToManyField(
        'AnimeVost',
        blank=True,
    )
    series = models.ManyToManyField(
        'Series',
        blank=True,
        related_name='anime'
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
        upload_to='preview/',
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
        choices=WEEK_CHOICES,
        default=None,
        blank=True,
        null=True,
    )
    anons = models.BooleanField(default=False)
    indefinite_exit = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_en if self.title_en else self.title_ru
