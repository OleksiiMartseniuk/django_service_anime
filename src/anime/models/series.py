from django.db import models


class Series(models.Model):
    ANIME_VOST = 'anime_vost'
    PROJECT_ANIME_CHOICES = (
        (ANIME_VOST, "AnimeVost"),
    )

    name = models.CharField(max_length=50)
    number = models.IntegerField(
        blank=True,
        null=True,
    )
    serial_number = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    project_anime = models.CharField(
        choices=PROJECT_ANIME_CHOICES,
        max_length=20,
    )
    anime_id = models.IntegerField()

    def __str__(self):
        return (
            f"Series{self.name} - "
            f"ProjectAnime[{self.project_anime}] - "
            f"Anime[{self.anime_id}]"
        )

    def get_anime_vost_quality(self, quality: str) -> str | None:
        # TODO: check it
        QUALITY = {
            "sd": f"http://video.aniland.org/360/{self.serial_number}.mp4",
            "hd": f"http://video.aniland.org/720/{self.serial_number}.mp4",
        }
        return QUALITY.get(quality)

    def get_anime_vost_preview(self):
        return f"http://media.aniland.org/img/{self.serial_number}.jpg"
