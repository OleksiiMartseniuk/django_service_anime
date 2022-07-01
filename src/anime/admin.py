from django.contrib import admin
from .models import Anime, Genre, Series, ScreenImages


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'id_anime', 'rating', 'votes', 'day_week', 'anons'
    )
    list_filter = ('day_week', 'anons', 'rating', 'votes')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(ScreenImages)
class ScreenImagesAdmin(admin.ModelAdmin):
    list_display = ('images',)
