from rest_framework import serializers

from src.anime.models import Anime

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
        exclude = ['track', 'staff']


class GetBotUserSerializer(serializers.ModelSerializer):
    """Вывод пользователя"""
    class Meta:
        model = BotUser
        exclude = ['track']


class TrackedAnimeUserSerializer(serializers.Serializer):
    anime_ids = serializers.ListField(child=serializers.IntegerField())
    user_id = serializers.IntegerField()


class TrackedUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    subscriber = serializers.BooleanField()


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'title', 'anons', 'link',
                  'timer', 'rating', 'votes', 'url_image_preview',
                  'telegram_id_file', 'day_week']
