from rest_framework.test import APITestCase

from django.urls import reverse

from src.anime.models import Anime, Series, Genre
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
        url = reverse('series')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()['results']
        self.assertEqual(response.json()['count'], 3)
        self.assertEqual(data[0]['name'], objs[1].name)
        self.assertEqual(data[1]['name'], objs[0].name)
        self.assertEqual(data[2]['name'], objs[2].name)

    def test_anime_series_list_view_id_anime(self):
        objs = Series.objects.bulk_create([
            Series(id_anime=1, name='12 t', std='test', hd='test', number=12),
            Series(id_anime=1, name='5 t', std='test', hd='test', number=5),
            Series(id_anime=1, name='OVA', std='test', hd='test', number=None),
        ])
        url = reverse('series')
        response = self.client.get(url, {'id_anime': 1})
        self.assertEqual(response.status_code, 200)
        data = response.json()['results']
        self.assertEqual(response.json()['count'], 3)
        self.assertEqual(data[0]['name'], objs[1].name)
        self.assertEqual(data[1]['name'], objs[0].name)
        self.assertEqual(data[2]['name'], objs[2].name)

    def test_genre_list_view(self):
        objs = Genre.objects.bulk_create([
            Genre(title='test'),
            Genre(title='test1')
        ])
        url = reverse('genre-list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['title'], objs[0].title)
        self.assertEqual(data[1]['title'], objs[1].title)

    def test_anime_list_view(self):
        config_data.create_anime()
        url = reverse('anime')
        response = self.client.get(url)
        data = response.json()['results']
        self.assertEqual(response.json()['count'], 2)
        self.assertTrue(Anime.objects.filter(id=data[0]['id']).exists())
        self.assertTrue(Anime.objects.filter(id=data[1]['id']).exists())

    def test_anime_list_view_day_week(self):
        config_data.create_anime()
        url = reverse('anime')
        response = self.client.get(url, {'day_week': 'monday'})
        data = response.json()['results']
        self.assertEqual(response.json()['count'], 2)
        self.assertTrue(Anime.objects.filter(id=data[0]['id']).exists())
        self.assertTrue(Anime.objects.filter(id=data[1]['id']).exists())

    def test_anime_list_view_anons(self):
        config_data.create_anime()
        url = reverse('anime')
        response = self.client.get(url, {'anons': True})
        data = response.json()['results']
        self.assertEqual(response.json()['count'], 2)
        self.assertTrue(Anime.objects.filter(id=data[0]['id']).exists())
        self.assertTrue(Anime.objects.filter(id=data[1]['id']).exists())

    def test_anime_list_view_search(self):
        config_data.create_anime()
        url = reverse('anime')
        response = self.client.get(url, {'search': 'title1'})
        data = response.json()['results']
        self.assertEqual(response.json()['count'], 1)
        self.assertTrue(Anime.objects.filter(id=data[0]['id']).exists())

    def test_anime_list_view_genre(self):
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
        genre = Genre.objects.create(title='test')
        anime.genre.add(genre)
        url = reverse('anime')
        response = self.client.get(url, {'genre': 'test'})
        data = response.json()['results']
        self.assertEqual(response.json()['count'], 1)
        self.assertTrue(Anime.objects.filter(id=data[0]['id']).exists())
