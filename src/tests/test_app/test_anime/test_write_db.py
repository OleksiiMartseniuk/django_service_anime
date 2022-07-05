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

        self.writer._write_genre.cache_clear()
        result = self.writer._write_genre('приключения')
        self.assertEqual(1, Genre.objects.count())

        genre = Genre.objects.filter(title='приключения')[0]
        self.assertEqual(result.title, genre.title)
        self.assertEqual(result.id, genre.id)

    def test_write_genre_decorator(self):
        self.assertEqual(0, Genre.objects.count())

        self.writer._write_genre.cache_clear()
        result1 = self.writer._write_genre('приключения')
        result2 = self.writer._write_genre('приключения')
        result3 = self.writer._write_genre('приключения')
        self.assertEqual(1, Genre.objects.count())

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

        anime = self.writer.write_anime(config_data.write_anime_shem)

        self.assertEqual(anime.screen_image.count(), 1)
        self.assertEqual(anime.genre.count(), 2)

    @mock.patch('src.anime.service.write_db.WriteDB._write_anime')
    def test_write_anime_composed(self, mock_write_anime):
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
        anime = Anime.objects.create(
            id_anime=2,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as'
        )

        self.assertEqual(anime.anime_composed.count(), 0)

        self.writer._write_anime_composed(
            anime,
            config_data.write_anime_composed
        )

        self.assertEqual(anime.anime_composed.count(), 1)

    def test_write_anime_composed_empty(self):
        anime = Anime.objects.create(
            id_anime=2,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as'
        )

        self.assertEqual(anime.anime_composed.count(), 0)

        self.writer._write_anime_composed(anime, [])

        self.assertEqual(anime.anime_composed.count(), 0)

    def test_write_anime_schedule(self):
        self.assertEqual(Anime.objects.count(), 0)
        self.assertEqual(Genre.objects.count(), 0)
        self.assertEqual(ScreenImages.objects.count(), 0)

        self.writer._write_genre.cache_clear()
        self.writer.write_anime_schedule(config_data.write_anime_schedule_data)

        self.assertEqual(Genre.objects.count(), 3)
        self.assertEqual(ScreenImages.objects.count(), 4)
        self.assertEqual(Anime.objects.count(), 2)

        base_anime = Anime.objects.filter(
            id_anime=config_data.write_anime_schedule_data['monday'][0].id
        )[0]

        self.assertEqual(base_anime.anime_composed.count(), 1)
        self.assertEqual(base_anime.genre.count(), 2)
        self.assertEqual(base_anime.screen_image.count(), 3)
        self.assertEqual(base_anime.day_week, 'monday')
        self.assertFalse(base_anime.anons)

        id_con = config_data.write_anime_schedule_data['monday'][0]
        anime_composed = Anime.objects.filter(
            id_anime=id_con.anime_composed[0].id
        )[0]

        self.assertEqual(anime_composed.anime_composed.count(), 0)
        self.assertEqual(anime_composed.genre.count(), 3)
        self.assertEqual(anime_composed.screen_image.count(), 1)
        self.assertEqual(anime_composed.day_week, '')
        self.assertFalse(anime_composed.anons)

    def test_write_anime_schedule_exists(self):
        Anime.objects.create(
            id_anime=2696,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as'
        )
        self.assertEqual(Anime.objects.count(), 1)
        self.writer.write_anime_schedule(config_data.write_anime_schedule_data)
        self.assertEqual(Anime.objects.count(), 1)

    def test_write_anime_anons(self):
        anons_list = config_data.write_anime_anons_data

        self.assertEqual(Anime.objects.count(), 0)
        self.assertEqual(Genre.objects.count(), 0)
        self.assertEqual(ScreenImages.objects.count(), 0)

        self.writer._write_genre.cache_clear()
        self.writer.write_anime_anons(anons_list)

        self.assertEqual(Genre.objects.count(), 3)
        self.assertEqual(ScreenImages.objects.count(), 4)
        self.assertEqual(Anime.objects.count(), 2)

        base_anime = Anime.objects.filter(
            id_anime=anons_list[0].id
        )[0]

        self.assertEqual(base_anime.anime_composed.count(), 1)
        self.assertEqual(base_anime.genre.count(), 2)
        self.assertEqual(base_anime.screen_image.count(), 3)
        self.assertEqual(base_anime.day_week, '')
        self.assertTrue(base_anime.anons)

        anime_composed = Anime.objects.filter(
            id_anime=anons_list[0].anime_composed[0].id
        )[0]

        self.assertEqual(anime_composed.anime_composed.count(), 0)
        self.assertEqual(anime_composed.genre.count(), 3)
        self.assertEqual(anime_composed.screen_image.count(), 1)
        self.assertEqual(anime_composed.day_week, '')
        self.assertFalse(anime_composed.anons)

    def test_write_anime_anons_not(self):
        anons_list = config_data.write_anime_schedule_data['monday']

        self.assertEqual(Anime.objects.count(), 0)
        self.assertEqual(Genre.objects.count(), 0)
        self.assertEqual(ScreenImages.objects.count(), 0)

        self.writer._write_genre.cache_clear()
        self.writer.write_anime_anons(anons_list)

        self.assertEqual(Anime.objects.count(), 0)
        self.assertEqual(Genre.objects.count(), 0)
        self.assertEqual(ScreenImages.objects.count(), 0)

    def test_write_anime_full_not(self):
        anons_data = config_data.write_anime_schedule_data['monday'][0]

        Anime.objects.create(
            id_anime=2696,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as'
        )

        self.assertEqual(Anime.objects.count(), 1)
        self.writer.write_anime_full(anons_data)
        self.assertEqual(Anime.objects.count(), 1)

    def test_write_anime_full(self):
        anons_data = config_data.write_anime_schedule_data['monday'][0]

        self.assertEqual(Anime.objects.count(), 0)
        self.assertEqual(Genre.objects.count(), 0)
        self.assertEqual(ScreenImages.objects.count(), 0)

        self.writer._write_genre.cache_clear()
        self.writer.write_anime_full(anons_data)

        self.assertEqual(Genre.objects.count(), 3)
        self.assertEqual(ScreenImages.objects.count(), 4)
        self.assertEqual(Anime.objects.count(), 2)

        base_anime = Anime.objects.filter(
            id_anime=anons_data.id
        )[0]

        self.assertEqual(base_anime.anime_composed.count(), 1)
        self.assertEqual(base_anime.genre.count(), 2)
        self.assertEqual(base_anime.screen_image.count(), 3)
        self.assertEqual(base_anime.day_week, '')
        self.assertFalse(base_anime.anons)

        anime_composed = Anime.objects.filter(
            id_anime=anons_data.anime_composed[0].id
        )[0]

        self.assertEqual(anime_composed.anime_composed.count(), 0)
        self.assertEqual(anime_composed.genre.count(), 3)
        self.assertEqual(anime_composed.screen_image.count(), 1)
        self.assertEqual(anime_composed.day_week, '')
        self.assertFalse(anime_composed.anons)

    def test_write_anime_anons_not_id(self):
        anons_data = config_data.write_anime_schedule_data['monday']

        Anime.objects.create(
            id_anime=2696,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as',
            anons=True
        )

        self.assertEqual(Anime.objects.count(), 1)
        self.writer.write_anime_anons(anons_data)
        self.assertEqual(Anime.objects.count(), 1)
