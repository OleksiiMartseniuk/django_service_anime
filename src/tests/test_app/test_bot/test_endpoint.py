import json

from rest_framework.test import APITestCase

from django.urls import reverse
from django.contrib.auth import get_user_model

from django_celery_beat.models import CrontabSchedule, PeriodicTask

from src.bot.models import (
    BotStatistics,
    BotCollBackMessage,
    BotUser,
    BotUserAnimePeriodTask
)

from . import config_data

User = get_user_model()


class TestEndPoint(APITestCase):
    def authenticate(self, username, password):
        url = reverse('auth')
        response = self.client.post(
            url,
            data={'username': username, 'password': password}
        )
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + response.data['token']
        )

    def create_user(
            self,
            username: str = 'test',
            password: str = 'password'
    ) -> User:
        return User.objects.create_user(username=username, password=password)

    def test_statistics_bot_view(self):
        self.create_user()
        self.authenticate('test', 'password')
        self.assertEqual(BotStatistics.objects.count(), 0)
        url = reverse('create-statistic')
        data = {
            "id_user": 12345,
            "action": "test",
            "message": "test-message"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BotStatistics.objects.count(), 1)
        data_json = response.json()
        self.assertEqual(data_json['id_user'], data['id_user'])
        self.assertEqual(data_json['action'], data['action'])
        self.assertEqual(data_json['message'], data['message'])
        self.client.credentials()

    def test_bot_coll_back_message_view(self):
        self.create_user()
        self.authenticate('test', 'password')
        self.assertEqual(BotCollBackMessage.objects.count(), 0)
        url = reverse('create-massage')
        data = {
            "id_user": 12345,
            "message": "test-message"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BotCollBackMessage.objects.count(), 1)
        data_json = response.json()
        self.assertEqual(data_json['id_user'], data['id_user'])
        self.assertEqual(data_json['message'], data['message'])
        self.client.credentials()

    def test_bot_user_create(self):
        self.create_user()
        self.authenticate('test', 'password')
        self.assertEqual(BotUser.objects.count(), 0)
        url = reverse('create-user')
        data = {
            'username': 'test',
            'user_id': 1234567,
            'chat_id': 7654321
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BotUser.objects.count(), 1)
        data_json = response.json()
        self.assertEqual(data_json['username'], data['username'])
        self.assertEqual(data_json['user_id'], data['user_id'])
        self.assertEqual(data_json['chat_id'], data['chat_id'])
        self.client.credentials()

    def test_list_user(self):
        user = config_data.create_bot_user()
        self.create_user()
        self.authenticate('test', 'password')
        url = reverse('user-bot')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()[0]
        self.assertEqual(data['id'], user.id)
        self.assertEqual(data['username'], user.username)
        self.assertEqual(data['user_id'], user.user_id)
        self.assertEqual(data['chat_id'], user.chat_id)
        self.assertEqual(data['staff'], user.staff)

    def test_add_anime_user_view(self):
        anime = config_data.create_anime(timer=1663277581)
        user = config_data.create_bot_user()
        self.create_user()
        self.authenticate('test', 'password')
        self.assertEqual(user.track.count(), 0)
        url = reverse('add-anime')
        data = {
            'anime_ids': [anime.id],
            'user_id': user.user_id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(user.track.count(), 1)
        self.client.credentials()

    def test_remove_anime_user_view(self):
        anime = config_data.create_anime(timer=1663277581)
        user = config_data.create_bot_user()
        schedule = CrontabSchedule.objects.create(
            minute=33,
            hour=0,
            day_of_week=4
        )
        period_task = PeriodicTask.objects.create(
            crontab=schedule,
            name=f'{anime.id}_{user.id}',
            task='src.bot.tasks.reminders',
            args=json.dumps([user.chat_id, anime.id]),
        )
        BotUserAnimePeriodTask.objects.create(
            user=user,
            anime=anime,
            period_task=period_task
        )
        self.assertEqual(PeriodicTask.objects.count(), 1)
        self.assertEqual(BotUserAnimePeriodTask.objects.count(), 1)

        self.create_user()
        self.authenticate('test', 'password')

        url = reverse('remove-anime')
        data = {
            'anime_ids': [anime.id],
            'user_id': user.user_id,
        }
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(PeriodicTask.objects.count(), 0)
        self.assertEqual(BotUserAnimePeriodTask.objects.count(), 0)
        self.client.credentials()

    def test_get_anime_user_view_true(self):
        anime = config_data.create_anime(timer=1663277581)
        user = config_data.create_bot_user()
        schedule = CrontabSchedule.objects.create(
            minute=33,
            hour=0,
            day_of_week=4
        )
        period_task = PeriodicTask.objects.create(
            crontab=schedule,
            name=f'{anime.id}_{user.id}',
            task='src.bot.tasks.reminders',
            args=json.dumps([user.chat_id, anime.id]),
        )
        BotUserAnimePeriodTask.objects.create(
            user=user,
            anime=anime,
            period_task=period_task
        )

        self.create_user()
        self.authenticate('test', 'password')

        url = reverse('get-anime', args=[user.user_id, True])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()[0]
        self.assertEqual(data['id'], anime.id)
        self.assertEqual(data['title'], anime.title)
        self.client.credentials()

    def test_get_anime_user_view_false(self):
        anime = config_data.create_anime(timer=1663277581)
        user = config_data.create_bot_user()

        self.create_user()
        self.authenticate('test', 'password')

        url = reverse('get-anime', args=[user.user_id, False])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()[0]
        self.assertEqual(data['id'], anime.id)
        self.assertEqual(data['title'], anime.title)
        self.client.credentials()
