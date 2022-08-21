import logging

from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse

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
        ]
        return my_urls + urls

    def bot(self, request):
        form = BotForm()
        if request.method == 'POST':
            form = BotForm(request.POST)
            if form.is_valid():
                action = form.data['action']
                status = service.form_control_bot(action)
                self.message_user(request, status.message, level=status.level)

                logger.info(f'Пользователь [{request.user.username}]-'
                            f'[{form.data["action"]}]')
        context = dict(
            self.admin_site.each_context(request),
            form=form
        )
        return TemplateResponse(request, 'admin/bot.html', context)


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
