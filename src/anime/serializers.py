from rest_framework import serializers

from .models import Anime, ScreenImages, Genre


class ScreenImageSerializers(serializers.ModelSerializer):
    """Вывод набор кадров"""
    class Meta:
        model = ScreenImages
        fields = '__all__'


class GenreSerializers(serializers.ModelSerializer):
    """Вывод жанров"""
    class Meta:
        model = Genre
        fields = '__all__'


class AnimeComposedSerializers(serializers.ModelSerializer):
    """Вывод аниме состоит"""
    class Meta:
        model = Anime
        fields = ['id', 'title']


class AnimeSerializers(serializers.ModelSerializer):
    """Вывод полного описания Anime"""
    screen_image = ScreenImageSerializers(read_only=True, many=True)
    genre = GenreSerializers(read_only=True, many=True)
    anime_composed = AnimeComposedSerializers(read_only=True, many=True)

    class Meta:
        model = Anime
        fields = '__all__'


class AnimeMinAnonsSerializers(serializers.ModelSerializer):
    """Вывод короткого описания"""
    class Meta:
        model = Anime
        fields = ['id', 'title', 'url_image_preview']
