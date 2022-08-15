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
        obj = ScreenImages.objects.create(images='http://test.gif')
        self.assertFalse(obj.images_s)
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\
            x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\
            x44\x01\x00\x3b')
        utils.download_image(obj.images_s, obj.images)
        self.assertTrue(obj.images_s)

        file_path = 'media/screen_images/test.gif'
        if os.path.isfile(file_path):
            os.remove(file_path)

    @mock.patch('src.anime.service.utils.os.remove')
    def test_delete_img_files(self, mock_remove):
        utils.delete_img_files()
        mock_remove.assert_called()
