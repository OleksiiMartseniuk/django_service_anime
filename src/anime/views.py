from rest_framework import generics

from .models import Anime
from .serializers import AnimeSerializers, AnimeMinAnonsSerializers


class AnimeAnonsListView(generics.ListAPIView):
    """Вывод списка аниме анонсов"""
    queryset = Anime.objects.filter(anons=True).values('id', 'title',
                                                       'url_image_preview')
    serializer_class = AnimeMinAnonsSerializers


class AnimeDetailView(generics.RetrieveAPIView):
    """Вывод аниме"""
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers
