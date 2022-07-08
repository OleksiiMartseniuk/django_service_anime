from rest_framework.test import APITestCase
from unittest import mock

from src.anime.service.service import ServiceAnime
from src.anime.models import Anime, ScreenImages, Genre

from . import config_data


class TestServiceAnime(APITestCase):
    @mock.patch(
        'src.anime.service.service.ServiceAnimeVost.get_data_anime_all')
    @mock.patch('src.anime.service.service.WriteDB.write_anime_schedule')
    def test_anime_schedule(
            self,
            mock_write_anime_schedule,
            mock_get_data_anime_all
    ):
        ServiceAnime().anime_schedule()
        mock_write_anime_schedule.assert_called_once()
        mock_get_data_anime_all.assert_called_once()

    @mock.patch(
        'src.anime.service.service.ServiceAnimeVost.get_data_anime_anons_all')
    @mock.patch('src.anime.service.service.WriteDB.write_anime_anons')
    def test_anime_anons(
            self,
            mock_write_anime_anons,
            mock_get_data_anime_anons_all
    ):
        ServiceAnime().anime_anons()
        mock_get_data_anime_anons_all.assert_called_once()
        mock_write_anime_anons.assert_called_once()

    @mock.patch('src.anime.service.service.WriteDB.clear_cash_memory')
    def test_delete_table(self, mock_clear_cash_memory):
        genre = Genre.objects.create(title='genre')
        image = ScreenImages.objects.create(images='img')
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
        anime.genre.add(genre)
        anime.screen_image.add(image)

        self.assertEqual(Anime.objects.count(), 1)
        self.assertEqual(Genre.objects.count(), 1)
        self.assertEqual(ScreenImages.objects.count(), 1)

        ServiceAnime().delete_table()
        mock_clear_cash_memory.assert_called_once()

        self.assertEqual(Anime.objects.count(), 0)
        self.assertEqual(Genre.objects.count(), 0)
        self.assertEqual(ScreenImages.objects.count(), 0)

    @mock.patch('src.anime.service.service.ServiceAnimeVost.get_anime_data')
    @mock.patch('src.anime.service.service.WriteDB.write_anime_full')
    def test_write_anime_none(
            self,
            mock_get_anime_data,
            mock_write_anime_full
    ):
        ServiceAnime()._write_anime([])
        self.assertFalse(mock_get_anime_data.called)
        self.assertFalse(mock_write_anime_full.called)

    @mock.patch('src.anime.service.service.ServiceAnimeVost.get_anime_data')
    @mock.patch('src.anime.service.service.WriteDB.write_anime_full')
    def test_write_anime(
            self,
            mock_get_anime_data,
            mock_write_anime_full
    ):
        ServiceAnime()._write_anime([config_data.create_schemas])
        mock_get_anime_data.assert_called_once()
        mock_write_anime_full.assert_called_once()
