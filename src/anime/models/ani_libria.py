from django.db import models


class StatusChoices(models.IntegerChoices):
    IN_PROGRESS = (1, "In progress")
    COMPLETED = (2, "Completed")
    IS_HIDDEN = (3, "Is hidden")
    UN_ONGOING = (4, "Un ongoing")


class SeasonChoices(models.IntegerChoices):
    WINTER = (1, "Winter")
    SPRING = (2, "Spring")
    SUMMER = (3, "Summer")
    AUTUMN = (4, "Autumn")


class WeekDayChoices(models.IntegerChoices):
    MONDAY = (0, "Monday")
    TUESDAY = (1, "Tuesday")
    WEDNESDAY = (2, "Wednesday")
    THURSDAY = (3, "Thursday")
    FRIDAY = (4, "Friday")
    SATURDAY = (5, "Saturday")
    SUNDAY = (6, "Sunday")


class AnimeTypeChoices(models.IntegerChoices):
    MOVIE = (0, "Movie")
    TV = (1, "TV")
    OVA = (2, "OVA")
    ONA = (3, "ONA")
    SPECIAL = (4, "Special")
    WEB = (5, "WEB")


class AniLibria(models.Model):
    anime_id = models.IntegerField(unique=True)
    code = models.CharField(max_length=255)
    name_ru = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    name_en = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    name_alternative = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    announce = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    status = models.IntegerField(choices=StatusChoices.choices)
    updated = models.DateTimeField(
        blank=True,
        null=True,
    )
    last_change = models.DateTimeField(
        blank=True,
        null=True,
    )
    anime_type = models.IntegerField(choices=AnimeTypeChoices.choices)
    genres = models.ManyToManyField(
        'Genre',
        related_name='anilibria',
        blank=True
    )
    team = models.ForeignKey(
        'Team',
        related_name='anilibria',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    season = models.IntegerField(choices=SeasonChoices.choices)
    week_day = models.IntegerField(
        choices=WeekDayChoices.choices,
        blank=True,
        null=True,
    )
    description = models.TextField()
    in_favorites = models.IntegerField()
    blocked = models.BooleanField(
        default=False,
        help_text="The title is blocked in the Russian Federation",
    )
    bakanim = models.BooleanField(
        default=False,
        help_text="Title blocked due to Wakanim complaints",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.id}] {self.name_en}"
