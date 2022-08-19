# Generated by Django 4.0.5 on 2022-08-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotCollBackMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='id пользователя')),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BotStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='id пользователя')),
                ('action', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
