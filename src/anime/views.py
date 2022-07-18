from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import filters

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .service.pagination import (
    LargeResultsSetPagination,
    StandardResultsSetPagination
)
from .models import Anime, Series, Genre
from .service import service
from .serializers import (
    AnimeSerializers,
    AnimeMinSerializers,
    SeriesSerializers,
    GenreSerializers
)


class AnimeDetailView(generics.RetrieveAPIView):
    """
    Вывод аниме
    ---
    """
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers


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


class AnimeListView(generics.ListAPIView):
    """
    Вывод всех аниме
    ---
    """
    queryset = Anime.objects.only('id', 'title',
                                  'url_image_preview',
                                  'url_image_preview_s',
                                  'timer').order_by('id')
    serializer_class = AnimeMinSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = service.AnimeFilter
    pagination_class = StandardResultsSetPagination
    search_fields = ['@title']


class GenreListView(generics.ListAPIView):
    """
    Вывод списка жанров
    ---
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
