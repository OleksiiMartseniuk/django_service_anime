from django.contrib import admin
from django.utils.safestring import mark_safe

from solo.admin import SingletonModelAdmin

from .models import (
    BotStatistics,
    BotCollBackMessage,
    BotUser,
    BotUserAnimePeriodTask,
    BotSettings
)


@admin.register(BotSettings)
class AdminBotSettings(SingletonModelAdmin):
    fieldsets = (
        ("Setting", {"fields": ("token", "chat_id")}),
        ("People", {"fields": ("count_action_people",)})
    )
    readonly_fields = ("count_action_people",)

    @staticmethod
    def count_action_people(instance):
        count = BotStatistics.objects.values('id_user').distinct().count()
        return mark_safe(f"<b>{count}</b>")


@admin.register(BotStatistics)
class BotStatisticsAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'action', 'created')
    list_filter = ('id_user', 'action', 'created')
    search_fields = ('id_user', 'action')
    readonly_fields = ('id_user', 'action', 'message', 'created')


@admin.register(BotCollBackMessage)
class BotCollBackMessageAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'created', 'read')
    list_filter = ('id_user', 'created', 'read')
    search_fields = ('id_user',)
    readonly_fields = ('id_user', 'message', 'created',)


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ('user_id', 'chat_id')
    search_fields = ('user_id',)


@admin.register(BotUserAnimePeriodTask)
class BotUserAnimePeriodTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'anime')
    list_filter = ('user',)
