# Generated by Django 4.0.5 on 2022-09-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0027_anime_telegram_id_file'),
        ('bot', '0004_delete_botidimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('user_id', models.IntegerField(verbose_name='ID пользователя telegram')),
                ('chat_id', models.IntegerField(verbose_name='ChatID пользователя telegram')),
                ('anime', models.ManyToManyField(blank=True, to='anime.anime')),
            ],
        ),
    ]
