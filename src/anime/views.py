from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .service.pagination import LargeResultsSetPagination
from .models import Anime, Series
from .service import service
from .serializers import (
    AnimeSerializers,
    AnimeMinAnonsSerializers,
    DaySerializers,
    AnimeMinSerializers,
    SeriesSerializers
)


class AnimeAnonsListView(generics.ListAPIView):
    """
    Вывод списка аниме анонсов
    ---
    """
    queryset = Anime.objects.filter(anons=True).values('id', 'title',
                                                       'url_image_preview')
    serializer_class = AnimeMinAnonsSerializers


class AnimeDetailView(generics.RetrieveAPIView):
    """
    Вывод аниме
    ---
    """
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers


class AnimeScheduleDayView(APIView):
    """
    Вывод расписания по дню
    ---
    """
    @swagger_auto_schema(request_body=DaySerializers,
                         responses={200: AnimeMinSerializers(many=True)})
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


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'id_anime',
                openapi.IN_PATH,
                type=openapi.TYPE_INTEGER
            )
        ]
    ),
)
class AnimeSeriesListView(generics.ListAPIView):
    """
    Вывод серий по id_anime
    ---
    """
    serializer_class = SeriesSerializers
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        id_anime = self.kwargs['id_anime']
        queryset = Series.objects.filter(id_anime=id_anime).\
            values('id', 'name', 'std', 'hd', 'number').order_by('number')
        return queryset
