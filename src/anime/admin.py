import logging
import os

from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect

from django_celery_beat.models import PeriodicTask

from .models import Anime, Genre, Series, ScreenImages, Statistics
from .forms import ParserForm
from .service.admin.parser_control import ParserControl


logger = logging.getLogger('main')


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'id', 'id_anime', 'rating', 'votes', 'day_week', 'anons'
    )
    list_filter = ('day_week', 'anons')
    search_fields = ('title', 'id_anime')
    filter_horizontal = ['anime_composed', 'genre', 'screen_image']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('parser/', self.admin_site.admin_view(self.parser),
                 name='parser'),
            path('download/', self.admin_site.admin_view(self.download),
                 name='download'),
            path('views-log/', self.admin_site.admin_view(self.views_log),
                 name='views-log'),
            path('task-update', self.admin_site.admin_view(self.auto_update),
                 name='task-update')
        ]
        return my_urls + urls

    def parser(self, request):
        form = ParserForm()
        status_task = PeriodicTask.objects.get(name='add-every-day-morning')
        if request.method == 'POST':
            form = ParserForm(request.POST)
            if form.is_valid():
                action = form.data['action']
                status = ParserControl().control(action)
                self.message_user(request, status.message, level=status.level)
                # Добавления действия в статистику
                Statistics.objects.create(
                    author=request.user,
                    message=dict(form.fields['action'].choices)[action]
                )
                logger.info(f'Пользователь [{request.user.username}]-'
                            f'[{form.data["action"]}]')

        context = dict(
            self.admin_site.each_context(request),
            form=form,
            statistics=Statistics.objects.order_by('-created')[:10],
            status_task=status_task.enabled,
        )
        return TemplateResponse(request, 'admin/parser.html', context)

    def download(self, request):
        """Скачивание файла логов"""
        file_path = settings.FILENAME_LOGGING
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=None)
                content = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Disposition'] = content
                logger.info(f'Пользователь [{request.user.username}] -'
                            f' скачал файл логов')
                return response
        logger.error('Файла information.log не существует')
        self.message_user(request, 'Что-то пошло не так', level=40)
        return redirect('admin:parser')

    def views_log(self, request):
        """Просмотр файла логов"""
        with open(settings.FILENAME_LOGGING, 'r') as fl:
            file = fl.read()
        file = file.split('\n')[::-1]
        return TemplateResponse(request, 'admin/log.html', {'file': file})

    def auto_update(self, request):
        """Авто обновления"""
        status_task = PeriodicTask.objects.get(name='add-every-day-morning')
        status_task.enabled = False if status_task.enabled else True
        status_task.save()
        # Добавления действия в статистику
        Statistics.objects.create(
            author=request.user,
            message=f'Авто обновления [{status_task.enabled}]'
        )
        logger.info(f'Пользователь [{request.user.username}] -'
                    f' auto-update - [{status_task.enabled}]')
        return redirect('admin:parser')


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
