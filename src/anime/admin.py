import logging

from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .tasks import update_anime
from .models import (
    AnimeVost,
    AniLibria,
    SeriesAnimeVost,
    ScreenImagesAnimeVost,
    Genre,
)


logger = logging.getLogger("db")


admin.site.register(Genre)
admin.site.register(ScreenImagesAnimeVost)
admin.site.register(SeriesAnimeVost)
admin.site.register(AniLibria)
admin.site.register(AnimeVost)

# class GenreInline(admin.TabularInline):
#     model = AnimeVost.genre.through
#     extra = 0
#     verbose_name_plural = "Genre"
#
#
# class ScreenImagesInline(admin.TabularInline):
#     model = AnimeVost.screen_image.through
#     extra = 0
#     verbose_name_plural = "ScreenImages"
#
#
# class AnimeComposedInline(admin.TabularInline):
#     model = AnimeVost.anime_composed.through
#     fk_name = "to_animevost"
#     extra = 0
#     verbose_name_plural = "AnimeComposed"


# @admin.register(AnimeVost)
# class AnimeVostAdmin(admin.ModelAdmin):
#     list_display = (
#         'title_en', 'id', 'get_image',
#         'anime_id', 'rating', 'votes',
#         'day_week', 'anons',
#     )
#     list_filter = ('day_week', 'anons', 'genre__title', 'indefinite_exit')
#     search_fields = ('title_ru', 'title_en', 'anime_id', 'id')
#     readonly_fields = ['updated', 'created']
#     inlines = [AnimeComposedInline, GenreInline, ScreenImagesInline]
#     exclude = ["genre", "screen_image", "anime_composed", "anime_series"]
#     actions = ["update_anime"]
#
#     def get_image(self, instance: AnimeVost):
#         if instance.url_image_preview:
#             return mark_safe(
#                 f"<img src='{instance.url_image_preview.url}' width=50>"
#             )
#
#     get_image.short_description = "image"
#
#     @admin.action(description="Update anime")
#     def update_anime(self, request, queryset):
#         anime_ids = list(queryset.values_list("anime_id", flat=True))
#         update_anime.apply_async(kwargs={"anime_ids": anime_ids})
#         self.message_user(
#             request,
#             f"{len(anime_ids)} in progress",
#             messages.SUCCESS,
#         )


# @admin.register(Series)
# class SeriesAdmin(admin.ModelAdmin):
#     list_display = ("name", "project_anime", "anime_id")
#     list_filter = ("project_anime",)
#     search_fields = ("anime_id",)
#     readonly_fields = (
#         "anime_vost_preview",
#         "anime_vost_quality_new",
#         "anime_vost_quality_old",
#     )
#
#     def anime_vost_preview(self, obj: Series):
#         if obj.project_anime != Series.ANIME_VOST:
#             return "---"
#         return mark_safe(
#             f'<a target="_blank" href="{obj.get_anime_vost_preview}">'
#             f'AnimeVost Preview</a>'
#         )
#
#     @staticmethod
#     def __anime_vost_quality(obj: Series, is_prefix: bool = False):
#         if obj.project_anime != Series.ANIME_VOST:
#             return "---"
#
#         return mark_safe(
#             f'<a target="_blank" '
#             f'href="{obj.get_anime_vost_quality("sd", is_prefix)}">'
#             f'480</a><br>'
#             f'<a target="_blank" '
#             f'href="{obj.get_anime_vost_quality("hd", is_prefix)}">'
#             f'720</a><br>'
#             f'<a target="_blank" '
#             f'href="{obj.get_anime_vost_quality("fhd", is_prefix)}">'
#             f'1080</a><br>'
#         )
#
#     def anime_vost_quality_new(self, obj: Series):
#         return self.__anime_vost_quality(obj, is_prefix=True)
#
#     def anime_vost_quality_old(self, obj: Series):
#         return self.__anime_vost_quality(obj)
