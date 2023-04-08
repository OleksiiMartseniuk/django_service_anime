import logging

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters

from src.anime.models import Anime, Series


logger = logging.getLogger('main')


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AnimeFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__title', lookup_expr='in')
    anons = filters.BooleanFilter()
    indefinite_exit = filters.BooleanFilter()

    class Meta:
        model = Anime
        fields = ['genre', 'day_week', 'anons', 'indefinite_exit']


class SeriesFilter(filters.FilterSet):
    anime_id = filters.NumberFilter(method='get_id_anime_vost')

    def get_id_anime_vost(self, queryset, field_name, value):
        try:
            id_anime = Anime.objects.values_list(
                'id_anime', flat=True
            ).get(id=value)
            return queryset.filter(id_anime=id_anime)
        except Anime.DoesNotExist:
            logger.error(f"Аниме с таки id[{value}] не существует")
            raise ValidationError(
                detail={'massage_error': 'Not found anime'},
                code=status.HTTP_404_NOT_FOUND
            )

    class Meta:
        model = Series
        fields = ['anime_id']


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 50


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
