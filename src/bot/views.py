from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema

from src.bot.models import BotUser

from .serializers import (
    BotStatisticsSerializer,
    BotCollBackMessageSerializer,
    BotUserCreateSerializer,
    GetBotUserSerializer,
    TrackedAnimeUserSerializer,
    TrackedUserSerializer,
    AnimeSerializer
)

from .services import service


class StatisticsBotView(generics.CreateAPIView):
    """
    Запись статистики бота
    ---
    """
    serializer_class = BotStatisticsSerializer
    permission_classes = [IsAdminUser]


class BotCollBackMessageView(generics.CreateAPIView):
    """
    Запись сообщения пользователя бота
    ---
    """
    serializer_class = BotCollBackMessageSerializer
    permission_classes = [IsAdminUser]


class BotUserCreateView(generics.CreateAPIView):
    """
    Создания пользователя
    ---
    """
    serializer_class = BotUserCreateSerializer
    permission_classes = [IsAdminUser]


class BotUserListView(generics.ListAPIView):
    """
    Вывод пользователей telegram бота
    ---
    """
    queryset = BotUser.objects.all().values(
        'id', 'username', 'user_id', 'chat_id', 'staff'
    )
    permission_classes = [IsAdminUser]
    serializer_class = GetBotUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'staff']


class AddAnimeUserView(generics.GenericAPIView):
    """
    Добавить аниме в отслеживаемые пользователем
    ---
    """
    permission_classes = [IsAdminUser]
    serializer_class = TrackedAnimeUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            service.add_anime(
                serializer.data['anime_ids'],
                serializer.data['user_id']
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RemoveAnimeUserView(generics.GenericAPIView):
    """
    Удаления аниме с отслеживаемые пользователем
    ---
    """
    permission_classes = [IsAdminUser]
    serializer_class = TrackedAnimeUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            service.delate_anime(
                serializer.data['anime_ids'],
                serializer.data['user_id']
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GetAnimeUserView(generics.GenericAPIView):
    """
    Вывод аниме отслеживаемые пользователем
    ---
    """
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(responses={200: AnimeSerializer(many=True)})
    def get(self, request, user_id: int, subscriber: bool):
        serializer = TrackedUserSerializer(
            data={'user_id': user_id, 'subscriber': subscriber}
        )
        if serializer.is_valid():
            anime_list = service.get_anime_tracked(
                serializer.data['user_id'],
                serializer.data['subscriber']
            )
            serializer_anime_list = AnimeSerializer(anime_list, many=True)
            return Response(serializer_anime_list.data, status=200)
        return Response(serializer.errors, status=400)
