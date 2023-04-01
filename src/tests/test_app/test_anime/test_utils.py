import os
from unittest import mock
from rest_framework.test import APITestCase

from src.anime.service import utils
from src.anime.models import ScreenImages


class TestUtils(APITestCase):
    def test_get_number(self):
        result = utils.get_number('123 test')
        self.assertEqual(result, 123)

        result = utils.get_number('test')
        self.assertEqual(result, None)

    @mock.patch('src.anime.service.utils.requests.get')
    def test_download_image(self, mock_get):
        obj = ScreenImages.objects.create()
        self.assertFalse(obj.images)
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\
            x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\
            x44\x01\x00\x3b')
        utils.download_image(obj.images, 'http://test.gif')
        self.assertTrue(obj.images)

        file_path = 'media/screen_images/test.gif'
        if os.path.isfile(file_path):
            os.remove(file_path)


    def test_get_link(self):
        link = 'https://animevost.org/tip/tv/2761-tunshi-xingkong.html'
        result = utils.get_link(
            2761,
            'Пожиратель звёзд / Tunshi Xingkong [1-48 из 52+]'
        )
        self.assertEqual(result, link)

    @mock.patch('src.anime.service.utils.logger', mock.Mock())
    def test_none_get_link(self):
        result = utils.get_link(
            2761,
            'Пожиратель звёзд'
        )
        self.assertIsNone(result)
