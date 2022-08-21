import logging

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.template.response import TemplateResponse

from django_celery_beat.models import PeriodicTask

from src.anime.models import Statistics

from .forms import BotForm
from .services.admin import service
from .models import (
    BotStatistics,
    BotCollBackMessage,
    BotIdImage
)


logger = logging.getLogger('main')


@admin.register(BotStatistics)
class BotStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'action', 'created')
    list_filter = ('id_user', 'action', 'created')
    search_fields = ('id_user', 'action')
    readonly_fields = ('created',)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('bot/', self.admin_site.admin_view(self.bot), name='bot'),
            path('task-write/', self.admin_site.admin_view(self.auto_write),
                 name='task-write'),
        ]
        return my_urls + urls

    def bot(self, request):
        form = BotForm()
        status_task = PeriodicTask.objects.get(
            name='add-every-day-morning-bot'
        )
        if request.method == 'POST':
            form = BotForm(request.POST)
            if form.is_valid():
                action = form.data['action']
                status = service.form_control_bot(action)
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
            status_task=status_task.enabled
        )
        return TemplateResponse(request, 'admin/bot.html', context)

    def auto_write(self, request):
        """Авто обновления"""
        status_task = PeriodicTask.objects.get(
            name='add-every-day-morning-bot'
        )
        status_task.enabled = False if status_task.enabled else True
        status_task.save()
        # Добавления действия в статистику
        Statistics.objects.create(
            author=request.user,
            message=f'Авто запись[telegram] [{status_task.enabled}]'
        )
        logger.info(f'Пользователь [{request.user.username}] -'
                    f' auto-update - [{status_task.enabled}]')
        return redirect('admin:bot')


@admin.register(BotCollBackMessage)
class BotCollBackMessageAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'created', 'read')
    list_filter = ('id_user', 'created', 'read')
    search_fields = ('id_user',)
    readonly_fields = ('created',)


@admin.register(BotIdImage)
class BotIdImageAdmin(admin.ModelAdmin):
    list_display = ('id_anime',)
    search_fields = ('id_anime',)
