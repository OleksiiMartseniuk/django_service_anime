from django.db import models


class ScreenImages(models.Model):
    images = models.ImageField(upload_to='screen_images/')

    def __str__(self) -> str:
        return f"ScreenImages - {self.id}"
