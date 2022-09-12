import logging

from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from .models import BotStatistics, BotCollBackMessage, BotUser


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
            path('bot-info/', self.admin_site.admin_view(self.bot_info),
                 name='bot-info'),
        ]
        return my_urls + urls

    def bot_info(self, request):
        """Информация о боте"""
        context = dict(
            self.admin_site.each_context(request),
            count=BotStatistics.objects.values('id_user').distinct().count(),
        )
        return TemplateResponse(request, 'admin/bot.html', context)


@admin.register(BotCollBackMessage)
class BotCollBackMessageAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'created', 'read')
    list_filter = ('id_user', 'created', 'read')
    search_fields = ('id_user',)
    readonly_fields = ('created',)


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ('user_id', 'chat_id')
    search_fields = ('user_id',)
    filter_horizontal = ('anime',)
