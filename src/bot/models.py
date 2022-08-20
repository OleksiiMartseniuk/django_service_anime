from django.db import models


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


class BotIdImage(models.Model):
    """ID photo телеграм сервис"""
    id_photo = models.CharField('ID telegram', max_length=255)
    id_anime = models.IntegerField('ID anime')

    def __str__(self):
        return f'anime id-{self.id_anime}'
