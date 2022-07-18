from rest_framework.test import APITestCase

from django.urls import reverse

from src.anime.models import Anime, Series
from . import config_data


class TestEndPoint(APITestCase):
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

    def test_anime_series_list_view(self):
        objs = Series.objects.bulk_create([
            Series(id_anime=1, name='12 t', std='test', hd='test', number=12),
            Series(id_anime=1, name='5 t', std='test', hd='test', number=5),
            Series(id_anime=1, name='OVA', std='test', hd='test', number=None),
        ])
        url = reverse('series', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['count'], 3)
        self.assertEqual(data['results'][0]['name'], objs[2].name)
        self.assertEqual(data['results'][1]['name'], objs[1].name)
        self.assertEqual(data['results'][2]['name'], objs[0].name)
