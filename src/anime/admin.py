import logging

from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import AnimeVost, Series, ScreenImages, Genre
from .tasks import update_anime


logger = logging.getLogger("db")


admin.site.register(Series)
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
    actions = ["update_anime"]

    def get_image(self, instance: AnimeVost):
        if instance.url_image_preview:
            return mark_safe(
                f"<img src='{instance.url_image_preview.url}' width=50>"
            )

    get_image.short_description = "image"

    @admin.action(description="Update anime")
    def update_anime(self, request, queryset):
        anime_ids = list(queryset.values_list("anime_id", flat=True))
        update_anime.apply_async(kwargs={"anime_ids": anime_ids})
        self.message_user(
            request,
            f"{len(anime_ids)} in progress",
            messages.SUCCESS,
        )


@admin.register(ScreenImages)
class ScreenImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "project_anime", "anime_id", "images")
    list_filter = ("project_anime",)
    search_fields = ("anime_id",)
