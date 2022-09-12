from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    BotStatisticsSerializer,
    BotCollBackMessageSerializer,
    BotUserCreateSerializer,
    AddAnimeUserSerializer
)

from .services import utils


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


class BotUserCreateView(generics.CreateAPIView):
    """
    Создания пользователя
    ---
    """
    serializer_class = BotUserCreateSerializer
    permission_classes = [IsAuthenticated]


class AddAnimeUserView(generics.GenericAPIView):
    """
    Добавить аниме в отслеживаемые пользователем
    ---
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AddAnimeUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            utils.add_anime(
                serializer.data['anime_ids'],
                serializer.data['user_id']
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
