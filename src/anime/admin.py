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


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'id', 'id_anime', 'rating', 'votes', 'day_week', 'anons'
    )
    list_filter = ('day_week', 'anons', 'genre__title', 'indefinite_exit')
    search_fields = ('title', 'id_anime', 'id')
    filter_horizontal = ['anime_composed', 'genre', 'screen_image']
    readonly_fields = ['updated']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_anime')
    list_filter = ('id_anime',)
    search_fields = ('id_anime',)


@admin.register(ScreenImages)
class ScreenImagesAdmin(admin.ModelAdmin):
    list_display = ('images',)
    search_fields = ('images',)
