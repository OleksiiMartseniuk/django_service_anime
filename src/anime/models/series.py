from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(
        blank=True,
        null=True,
    )
    serial = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    preview = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    link = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
