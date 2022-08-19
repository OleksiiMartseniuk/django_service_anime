from django.contrib import admin

from .models import (
    BotStatistics,
    BotCollBackMessage
)


@admin.register(BotStatistics)
class BotStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'action', 'created')
    list_filter = ('id_user', 'action', 'created')
    search_fields = ('id_user', 'action')


@admin.register(BotCollBackMessage)
class BotCollBackMessageAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'created', 'read')
    list_filter = ('id_user', 'created', 'read')
    search_fields = ('id_user',)
