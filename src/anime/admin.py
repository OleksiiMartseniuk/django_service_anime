from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from .models import Anime, Genre, Series, ScreenImages, Statistics
from .forms import ParserForm
from .service.admin.parser_control import ParserControl


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'id_anime', 'rating', 'votes', 'day_week', 'anons'
    )
    list_filter = ('day_week', 'anons')
    search_fields = ('title', 'id_anime')

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('parser/', self.admin_site.admin_view(self.parser))
        ]
        return my_urls + urls

    def parser(self, request):
        form = ParserForm()

        if request.method == 'POST':
            form = ParserForm(request.POST)
            if form.is_valid():
                status = ParserControl().control(form.data['action'])
                self.message_user(request, status.message, level=status.level)

        context = dict(
            self.admin_site.each_context(request),
            form=form
        )
        return TemplateResponse(request, 'admin/parser.html', context)


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


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'created')
    list_filter = ('author', 'message', 'created')
