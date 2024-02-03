from django.db import models


class ScreenImagesAnimeVost(models.Model):
    images = models.ImageField(upload_to='screen_images/')

    anime = models.ForeignKey(
        "AnimeVost",
        related_name="screen_images",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"[{self.id}]ScreenImages [{self.anime_id}]AnimeVost"
