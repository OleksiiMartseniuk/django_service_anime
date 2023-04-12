from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Prefetch

from rest_framework import generics
from rest_framework import filters

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
    queryset = Anime.objects.prefetch_related(
        Prefetch('screen_image'),
        Prefetch('genre'),
        Prefetch(
            'anime_composed',
            queryset=Anime.objects.only('id', 'title').order_by('id_anime')
        )
    )
    serializer_class = AnimeSerializers


class AnimeSeriesListView(generics.ListAPIView):
    """
    Вывод серий по id_anime
    ---
    """
    serializer_class = SeriesSerializers
    pagination_class = service.LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = service.SeriesFilter
    queryset = Series.objects.values(
        'id', 'name', 'serial', 'preview', 'link', 'number'
    ).order_by('number')


class AnimeListView(generics.ListAPIView):
    """
    Вывод всех аниме
    ---
    """
    queryset = Anime.objects.only('id', 'title', 'rating',
                                  'url_image_preview', 'votes',
                                  'timer', 'anons', 'link',
                                  ).order_by('-updated')
    serializer_class = AnimeMinSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_class = service.AnimeFilter
    pagination_class = service.StandardResultsSetPagination
    search_fields = ['@title']
    ordering_fields = ['rating', 'votes', 'updated']


class GenreListView(generics.ListAPIView):
    """
    Вывод списка жанров
    ---
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
