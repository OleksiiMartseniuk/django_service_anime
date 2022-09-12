from rest_framework import serializers

from .models import BotStatistics, BotCollBackMessage, BotUser


class BotStatisticsSerializer(serializers.ModelSerializer):
    """Статистики бота"""
    class Meta:
        model = BotStatistics
        fields = '__all__'


class BotCollBackMessageSerializer(serializers.ModelSerializer):
    """Сообщения пользователя"""
    class Meta:
        model = BotCollBackMessage
        exclude = ['read', 'created']


class BotUserCreateSerializer(serializers.ModelSerializer):
    """Создания пользователя"""
    class Meta:
        model = BotUser
        exclude = ['anime']
