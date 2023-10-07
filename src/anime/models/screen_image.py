from django.db import models


class ScreenImages(models.Model):
    ANIME_VOST = 'anime_vost'
    PROJECT_ANIME_CHOICES = (
        (ANIME_VOST, "AnimeVost"),
    )

    images = models.ImageField(upload_to='screen_images/')
    project_anime = models.CharField(
        choices=PROJECT_ANIME_CHOICES,
        max_length=20,
    )
    anime_id = models.IntegerField()

    def __str__(self) -> str:
        return (
            f"ScreenImages[{self.id}] "
            f"ProjectAnime[{self.project_anime}] "
            f"Anime[{self.anime_id}]"
        )
