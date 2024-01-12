from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Team(models.Model):
    voice = models.ManyToManyField(
        Person,
        related_name='voice',
        blank=True,
    )
    translator = models.ManyToManyField(
        Person,
        related_name='translator',
        blank=True,
    )
    editing = models.ManyToManyField(
        Person,
        related_name='editing',
        blank=True,
    )
    decor = models.ManyToManyField(
        Person,
        related_name='decor',
        blank=True,
    )
    timing = models.ManyToManyField(
        Person,
        related_name='timing',
        blank=True,
    )
    
    def __str__(self):
        return f"Team {self.id}"
