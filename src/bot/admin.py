from django.contrib import admin

from .models import (
    BotStatistics,
    BotCollBackMessage,
    BotIdImage
)


@admin.register(BotStatistics)
class BotStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'action', 'created')
    list_filter = ('id_user', 'action', 'created')
    search_fields = ('id_user', 'action')
    readonly_fields = ('created',)


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
