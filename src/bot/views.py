from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    BotStatisticsSerializer,
    BotCollBackMessageSerializer,
    BotUserCreateSerializer
)


class StatisticsBotView(generics.CreateAPIView):
    """
    Запись статистики бота
    ---
    """
    serializer_class = BotStatisticsSerializer
    permission_classes = [IsAuthenticated]


class BotCollBackMessageView(generics.CreateAPIView):
    """
    Запись сообщения пользователя бота
    ---
    """
    serializer_class = BotCollBackMessageSerializer
    permission_classes = [IsAuthenticated]


class BotUserCreate(generics.CreateAPIView):
    """
    Создания пользователя
    ---
    """
    serializer_class = BotUserCreateSerializer
    permission_classes = [IsAuthenticated]
