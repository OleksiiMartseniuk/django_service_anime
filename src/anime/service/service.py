from django_filters import rest_framework as filters

from src.anime.models import Anime


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AnimeFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__title', lookup_expr='in')
    anons = filters.BooleanFilter()

    class Meta:
        model = Anime
        fields = ['genre', 'day_week', 'anons']
