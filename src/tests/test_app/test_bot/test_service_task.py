from rest_framework.test import APITestCase

from django_celery_beat.models import CrontabSchedule, PeriodicTask

from src.bot.models import BotUser
from src.bot.services import task

from . import config_data


class TestServiceTest(APITestCase):

    def test_create_crontab_schedule(self):
        self.assertEqual(CrontabSchedule.objects.count(), 0)
        schedule = task.create_crontab_schedule(1663277581, 'thursday')
        self.assertEqual(CrontabSchedule.objects.count(), 1)
        self.assertEqual(schedule.hour, '21')
        self.assertEqual(schedule.minute, '33')
        self.assertEqual(schedule.day_of_week, 'thursday')

    def test_create_crontab_schedule_default(self):
        self.assertEqual(CrontabSchedule.objects.count(), 0)
        schedule = task.create_crontab_schedule(0, 'thursday')
        self.assertEqual(CrontabSchedule.objects.count(), 1)
        self.assertEqual(schedule.hour, '10')
        self.assertEqual(schedule.minute, '0')
        self.assertEqual(schedule.day_of_week, 'thursday')

    def test_create_crontab_schedule_get(self):
        schedule = CrontabSchedule.objects.create(
            minute='0',
            hour='10',
            day_of_week='thursday'
        )
        self.assertEqual(CrontabSchedule.objects.count(), 1)
        schedule_test = task.create_crontab_schedule(0, 'thursday')
        self.assertEqual(CrontabSchedule.objects.count(), 1)
        self.assertEqual(schedule.hour, schedule_test.hour)
        self.assertEqual(schedule.minute, schedule_test.minute)
        self.assertEqual(schedule.day_of_week, schedule_test.day_of_week)

    def test_create_periodic_task(self):
        self.assertEqual(PeriodicTask.objects.count(), 0)
        schedule = CrontabSchedule.objects.create(
            minute='0',
            hour='10',
            day_of_week='thursday'
        )
        user: BotUser = config_data.create_bot_user()
        task_: PeriodicTask = task.create_periodic_task(1, schedule, user)
        self.assertEqual(PeriodicTask.objects.count(), 1)
        self.assertEqual(task_.name, f'1_{user.id}')
