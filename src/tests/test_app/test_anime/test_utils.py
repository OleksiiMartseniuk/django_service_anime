from unittest import TestCase

from src.anime.service.utils import get_number


class TestUtils(TestCase):
    def test_get_number(self):
        result = get_number('123 test')
        self.assertEqual(result, 123)

        result = get_number('test')
        self.assertEqual(result, None)
