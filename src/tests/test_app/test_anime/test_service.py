import os
from unittest import mock
from rest_framework.test import APITestCase
from rest_framework.exceptions import ValidationError

from src.anime.service import service
from src.anime.models import Anime, ScreenImages


class TestService(APITestCase):
    def test_get_anime_list_day_raise_error(self):
        self.assertRaises(ValidationError, service.get_anime_list_day, 'test')

    def test_get_anime_list_day(self):
        Anime.objects.bulk_create([
            Anime(
                id_anime=1,
                title='title',
                link='anime_data.link',
                rating=1,
                votes=1,
                description='anime_data.description',
                director='anime_data.director',
                url_image_preview='url_image_preview',
                year='anime_data.year',
                type='an',
                day_week='monday'
            ),
            Anime(
                id_anime=2,
                title='title1',
                link='anime_data.link',
                rating=1,
                votes=1,
                description='anime_data.description',
                director='anime_data.director',
                url_image_preview='url_image_preview1',
                year='anime_data.year1',
                type='an',
                day_week='monday'
            )
        ])
        result = service.get_anime_list_day('monday')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['title'], 'title')
        self.assertEqual(result[0]['url_image_preview'], 'url_image_preview')
        self.assertEqual(result[1]['title'], 'title1')
        self.assertEqual(result[1]['url_image_preview'], 'url_image_preview1')

    @mock.patch('src.anime.service.service.requests.get')
    def test_download_image(self, mock_get):
        obj = ScreenImages.objects.create(images='http://test.gif')
        self.assertFalse(obj.images_s)
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\
            x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\
            x44\x01\x00\x3b')
        service.download_image(obj.images_s, obj.images)
        self.assertTrue(obj.images_s)

        file_path = 'media/screen_images/test.gif'
        if os.path.isfile(file_path):
            os.remove(file_path)
