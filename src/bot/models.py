from django.db import models

from django_celery_beat.models import PeriodicTask

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
    track = models.ManyToManyField(
        Anime,
        through='BotUserAnimePeriodTask',
        through_fields=('user', 'anime'),
        blank=True
    )

    def __str__(self):
        return self.username


class BotUserAnimePeriodTask(models.Model):
    """Расширенная таблица м2м"""
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    # Дополнительное поле PeriodicTask
    period_task = models.ForeignKey(PeriodicTask, on_delete=models.CASCADE)

    def __str__(self):
        return f'Пользователь[{self.user.username}] - ' \
               f'Аниме[{self.anime.title}]'
