# Generated by Django 4.0.5 on 2022-08-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0020_alter_botcollbackmessage_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='indefinite_exit',
            field=models.BooleanField(default=False, verbose_name='Неопределенный выход'),
        ),
    ]