# Generated by Django 4.0.5 on 2022-08-19 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0025_anime_updated'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BotCollBackMessage',
        ),
        migrations.DeleteModel(
            name='BotStatistics',
        ),
    ]