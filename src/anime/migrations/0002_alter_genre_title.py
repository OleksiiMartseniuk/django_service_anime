# Generated by Django 4.0.5 on 2022-07-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='Названия'),
        ),
    ]
