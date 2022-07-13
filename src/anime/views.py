from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .models import Anime
from .service import service
from .serializers import (
    AnimeSerializers,
    AnimeMinAnonsSerializers,
    DaySerializers,
    AnimeMinSerializers
)


class AnimeAnonsListView(generics.ListAPIView):
    """Вывод списка аниме анонсов"""
    queryset = Anime.objects.filter(anons=True).values('id', 'title',
                                                       'url_image_preview')
    serializer_class = AnimeMinAnonsSerializers


class AnimeDetailView(generics.RetrieveAPIView):
    """Вывод аниме"""
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers


class AnimeScheduleDayView(APIView):
    """Вывод расписания по дню"""
    def post(self, request):
        serializer_day = DaySerializers(data=request.data)
        if serializer_day.is_valid():
            anime_list = service.get_anime_list_day(serializer_day.data['day'])
            serializer_anime = AnimeMinSerializers(anime_list, many=True)
            return Response(
                serializer_anime.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_day.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
