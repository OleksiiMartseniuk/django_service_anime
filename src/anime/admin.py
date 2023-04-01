import logging

from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

from solo.admin import SingletonModelAdmin

from .models import (
    Anime,
    Genre,
    Series,
    ScreenImages,
    AnimeSettings
)
from .constants import ACTIONS_ADMIN
from .service.admin.parser_control import ParserControl


logger = logging.getLogger('db')


@admin.register(AnimeSettings)
class AnimeSettingsAdmin(SingletonModelAdmin):
    fieldsets = (
        ("Status", {"fields": ("status_task", "send_images_telegram")}),
        ("Action", {"fields": ("authorize",)})
    )
    readonly_fields = ("authorize",)

    @staticmethod
    def authorize(instance):
        links = [
            f'<a href={reverse("admin:parser")}?action={action}>{title}</a><hr>'
            for action, title in ACTIONS_ADMIN
        ]
        return mark_safe("<br>".join(links))

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                'parser/',
                self.admin_site.admin_view(self.parser),
                name='parser'
            )
        ]
        return my_urls + urls

    def parser(self, request):
        if request.user.is_staff:
            action = request.GET.get("action")
            status = ParserControl().control(action)
            self.message_user(request, status.message, level=status.level)
        return redirect('admin:anime_animesettings_changelist')


class GenreInline(admin.TabularInline):
    model = Anime.genre.through
    extra = 0
    verbose_name_plural = "Жанры"


class ScreenImagesInline(admin.TabularInline):
    model = Anime.screen_image.through
    extra = 0
    verbose_name_plural = "Изображения"


class AnimeComposedInline(admin.TabularInline):
    model = Anime.anime_composed.through
    fk_name = "to_anime"
    extra = 0
    verbose_name_plural = "Аниме состоит из"


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'id', 'get_image',
        'id_anime', 'rating', 'votes',
        'day_week', 'anons'
    )
    list_filter = ('day_week', 'anons', 'genre__title', 'indefinite_exit')
    search_fields = ('title', 'id_anime', 'id')
    readonly_fields = ['updated']
    inlines = [AnimeComposedInline, GenreInline, ScreenImagesInline]
    exclude = ["genre", "screen_image", "anime_composed"]

    def get_image(self, instance: Anime):
        if instance.url_image_preview:
            return mark_safe(
                f"<img src='{instance.url_image_preview.url}' width=50>"
            )

    get_image.short_description = "image"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_title_anime')
    list_filter = ('id_anime',)
    search_fields = ('id_anime',)

    def get_title_anime(self, instance: Series):
        try:
            anime = Anime.objects.get(id_anime=instance.id_anime)
            title = anime.title.split('/')[0]
        except Anime.DoesNotExist:
            title = ''
            logger.error(f"Нет аниме с id_anime_vost {instance.id_anime}")
        except IndexError:
            title = ''
            logger.error(f"Невозможно розбить названия Anime[{anime.id}]")
        return title

    get_title_anime.short_description = "title"


@admin.register(ScreenImages)
class ScreenImagesAdmin(admin.ModelAdmin):
    list_display = ('images',)
    search_fields = ('images',)
