from rest_framework.test import APITestCase

from django.urls import reverse
from django.contrib.auth import get_user_model

from src.bot.models import BotStatistics, BotCollBackMessage


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
