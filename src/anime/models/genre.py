from django.db import models


class Genre(models.Model):
    title = models.CharField(
        unique=True,
        max_length=30,
    )

    def __str__(self):
        return self.title
