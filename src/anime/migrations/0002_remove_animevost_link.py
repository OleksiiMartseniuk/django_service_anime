# Generated by Django 4.0.5 on 2023-09-15 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animevost',
            name='link',
        ),
    ]
