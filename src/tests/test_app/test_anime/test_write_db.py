from rest_framework.test import APITestCase
from unittest import mock

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

    @mock.patch('src.anime.service.write_db.WriteDB._write_screen_images')
    @mock.patch('src.anime.service.write_db.WriteDB._write_anime')
    def test_write_anime(
            self,
            mock_write_anime,
            mock_write_screen_images
    ):
        mock_write_anime.return_value = Anime.objects.create(
            id_anime=1,
            title='anime_data.title',
            link='anime_data.link',
            rating=1,
            votes=1,
            description='anime_data.description',
            director='anime_data.director',
            url_image_preview='anime_data.url_image_preview',
            year='anime_data.year',
            type='an'
        )
        mock_write_screen_images.return_value = ScreenImages.objects.create(
            images='https://animevost.org.jpg'
        )
        anime = Anime.objects.filter(id_anime=1)[0]
        self.assertEqual(anime.screen_image.count(), 0)
        self.assertEqual(anime.genre.count(), 0)

        self.writer.write_anime(config_data.write_anime_shem)

        anime = Anime.objects.filter(id_anime=1)[0]
        self.assertEqual(anime.screen_image.count(), 1)
        self.assertEqual(anime.genre.count(), 2)
