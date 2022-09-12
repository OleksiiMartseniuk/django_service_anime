from django.db import models

from src.anime.models import Anime


class BotStatistics(models.Model):
    """Статистика бота"""
    id_user = models.IntegerField('id пользователя')
    action = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь [{self.id_user}] действия [{self.action}]'


class BotCollBackMessage(models.Model):
    """Сообщения пользователя"""
    id_user = models.IntegerField('id пользователя')
    message = models.TextField()
    read = models.BooleanField('Прочитано', default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь [{self.id_user}]'


class BotUser(models.Model):
    """Пользователь бота"""
    username = models.CharField('Имя пользователя', max_length=255)
    user_id = models.IntegerField('ID пользователя telegram')
    chat_id = models.IntegerField('ChatID пользователя telegram')
    anime = models.ManyToManyField(Anime, blank=True)

    def __str__(self):
        return self.username
