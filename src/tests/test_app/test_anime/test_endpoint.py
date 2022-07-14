from rest_framework.test import APITestCase

from django.urls import reverse

from src.anime.models import Anime
from . import config_data


class TestEndPoint(APITestCase):
    def test_anime_anons_list_view(self):
        config_data.create_anime()
        url = reverse('anons')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_anime_detail_view(self):
        anime = Anime.objects.create(
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
        )
        url = reverse('anime-id', args=[anime.id])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], anime.id)
        self.assertEqual(data['screen_image'], [])
        self.assertEqual(data['genre'], [])
        self.assertEqual(data['anime_composed'], [])
        self.assertEqual(data['id_anime'], anime.id_anime)
        self.assertEqual(data['title'], anime.title)
        self.assertEqual(data['link'], anime.link)
        self.assertEqual(data['rating'], anime.rating)
        self.assertEqual(data['votes'], anime.votes)
        self.assertEqual(data['description'], anime.description)
        self.assertEqual(data['director'], anime.director)
        self.assertEqual(data['url_image_preview'], anime.url_image_preview)
        self.assertEqual(data['year'], anime.year)
        self.assertEqual(data['timer'], anime.timer)
        self.assertEqual(data['type'], anime.type)

    def test_anime_schedule_day_view(self):
        config_data.create_anime()
        url = reverse('schedule-day')
        response = self.client.post(url, data={'day': 'monday'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
