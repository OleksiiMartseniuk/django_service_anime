from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from .models import Anime, Genre, Series, ScreenImages
from .forms import ParserForm


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
                pass

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
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(ScreenImages)
class ScreenImagesAdmin(admin.ModelAdmin):
    list_display = ('images',)
    search_fields = ('images',)
