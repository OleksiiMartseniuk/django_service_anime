from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters

from src.anime.models import Anime


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AnimeFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__title', lookup_expr='in')
    anons = filters.BooleanFilter()
    indefinite_exit = filters.BooleanFilter()

    class Meta:
        model = Anime
        fields = ['genre', 'day_week', 'anons', 'indefinite_exit']


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 50


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
