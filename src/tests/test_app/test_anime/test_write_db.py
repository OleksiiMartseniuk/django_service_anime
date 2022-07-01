from rest_framework.test import APITestCase

from src.anime.service.write_db import WriteDB
from src.anime.models import Genre, ScreenImages, Anime

from . import config_data


class TestWriteDB(APITestCase):
    def setUp(self) -> None:
        self.writer = WriteDB()

    def test_write_genre(self):
        self.assertEqual(0, Genre.objects.count())

        result = self.writer._write_genre('приключения')
        self.assertEqual(1, Genre.objects.count())

        genre = Genre.objects.filter(title='приключения')[0]
        self.assertEqual(result.title, genre.title)
        self.assertEqual(result.id, genre.id)

    def test_write_genre_decorator(self):
        Genre.objects.create(title='приключения')
        self.assertEqual(1, Genre.objects.count())

        result = self.writer._write_genre('приключения')
        self.assertEqual(1, Genre.objects.count())

        genre = Genre.objects.filter(title='приключения')[0]
        self.assertEqual(result.title, genre.title)
        self.assertEqual(result.id, genre.id)

    def test_write_screen_images(self):
        self.assertEqual(0, ScreenImages.objects.count())

        result = self.writer._write_screen_images('http://test')
        self.assertEqual(1, ScreenImages.objects.count())

        screen = ScreenImages.objects.filter(images='http://test')[0]
        self.assertEqual(result.images, screen.images)
        self.assertEqual(result.id, screen.id)

    def test_write_anime_day_not_anons(self):
        self.assertEqual(0, Anime.objects.count())
        result = self.writer._write_anime(
            config_data.write_anime_shem, 'monday'
        )
        self.assertEqual(1, Anime.objects.count())

        anime = Anime.objects.filter(
            id_anime=config_data.write_anime_shem.id
        )[0]

        self.assertEqual(result.id, anime.id)
        self.assertEqual(anime.day_week, 'monday')
        self.assertFalse(anime.anons)

    def test_write_anime_anons_not_day(self):
        self.assertEqual(0, Anime.objects.count())

        new_conf = config_data.write_anime_shem.copy()
        new_conf.title = 'Test [Анонс]'
        result = self.writer._write_anime(new_conf)

        self.assertEqual(1, Anime.objects.count())

        anime = Anime.objects.filter(
            id_anime=config_data.write_anime_shem.id
        )[0]
        self.assertEqual(result.id, anime.id)
        self.assertEqual(anime.day_week, '')
        self.assertTrue(anime.anons)

