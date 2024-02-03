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
