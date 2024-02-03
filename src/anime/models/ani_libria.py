from django.db import models

from src.anime.choices import (
    WeekDayChoices,
    SeasonChoices,
    StatusChoices,
    AnimeTypeChoices,
)


class Franchise(models.Model):
    franchise_id = models.CharField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.id}] {self.name}"


class AniLibriaType(models.Model):
    full_string = models.CharField(max_length=255)
    type = models.IntegerField(choices=AnimeTypeChoices.choices)
    episodes = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    length = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"[{self.id}] {self.full_string}"


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
    franchise = models.ForeignKey(
        Franchise,
        on_delete=models.CASCADE,
        related_name="ani_libria"
    )
    releases = models.ManyToManyField(
        "AniLibria",
        blank=True,
    )
    ordinal = models.IntegerField()
    announce = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    status = models.IntegerField(choices=StatusChoices.choices)
    updated = models.DateTimeField(
        help_text=(
            "Last tile update (Usually the title is updated"
            " when new releases are released)"
        ),
        blank=True,
        null=True,
    )
    last_change = models.DateTimeField(
        help_text=(
            "Last title change (For example, a description or announcement)"
        ),
        blank=True,
        null=True,
    )
    anime_type = models.ForeignKey(
        AniLibriaType,
        related_name="ani_libria",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    genres = models.ManyToManyField(
        "Genre",
        related_name="anilibria",
        blank=True
    )
    team = models.ForeignKey(
        "Team",
        related_name="anilibria",
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
