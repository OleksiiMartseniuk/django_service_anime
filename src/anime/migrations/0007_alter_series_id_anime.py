# Generated by Django 4.0.5 on 2022-07-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_series_id_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='id_anime',
            field=models.IntegerField(verbose_name='ID animevost'),
        ),
    ]
