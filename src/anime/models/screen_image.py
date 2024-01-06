from django.db import models


class ScreenImages(models.Model):
    images = models.ImageField(upload_to='screen_images/')

    animevost = models.ForeignKey(
        "AnimeVost",
        related_name="screen_images",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    anilibria = models.ForeignKey(
        "AniLibria",
        related_name="screen_images",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        title = f"ScreenImages[{self.id}]"
        if self.anilibria_id:
            title += f"AniLibria [{self.anilibria_id}]"
        elif self.animevost_id:
            title += f"AnimeVost [{self.animevost_id}]"
        return title
