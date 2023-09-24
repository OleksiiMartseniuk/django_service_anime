from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import AnimeVost, Series, ScreenImages, Genre


admin.site.register(Series)
admin.site.register(ScreenImages)
admin.site.register(Genre)


class GenreInline(admin.TabularInline):
    model = AnimeVost.genre.through
    extra = 0
    verbose_name_plural = "Genre"


class ScreenImagesInline(admin.TabularInline):
    model = AnimeVost.screen_image.through
    extra = 0
    verbose_name_plural = "ScreenImages"


class AnimeComposedInline(admin.TabularInline):
    model = AnimeVost.anime_composed.through
    fk_name = "to_animevost"
    extra = 0
    verbose_name_plural = "AnimeComposed"


@admin.register(AnimeVost)
class AnimeVostAdmin(admin.ModelAdmin):
    list_display = (
        'title_en', 'id', 'get_image',
        'anime_id', 'rating', 'votes',
        'day_week', 'anons',
    )
    list_filter = ('day_week', 'anons', 'genre__title', 'indefinite_exit')
    search_fields = ('title_ru', 'title_en', 'anime_id', 'id')
    readonly_fields = ['updated', 'created']
    inlines = [AnimeComposedInline, GenreInline, ScreenImagesInline]
    exclude = ["genre", "screen_image", "anime_composed", "series"]

    def get_image(self, instance: AnimeVost):
        if instance.url_image_preview:
            return mark_safe(
                f"<img src='{instance.url_image_preview.url}' width=50>"
            )

    get_image.short_description = "image"
