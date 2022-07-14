from django import forms
from .models import Anime, Series


class ParserForm(forms.Form):
    action = forms.ChoiceField(label='', widget=forms.Select, choices=[
        ('schedule', 'Запись аниме расписания'),
        ('anons', 'Запись аниме анонсов'),
        ('delete', 'Удаления всех записей таблиц (Anime, ScreenImages, Genre)'),
        ('schedule_update', 'Обновить аниме расписания'),
        ('anons_update', 'Обновить аниме анонсов'),
        ('series', 'Запись серий'),
        ('series_update', 'Обновления серий'),
        ('delete_series', 'Очистка данных таблицы Series'),
    ])

    def clean_action(self):
        action = self.cleaned_data['action']
        match action:
            case 'schedule':
                self.schedule_valid()
            case 'anons':
                self.anons_valid()
            case 'delete':
                self.delete_valid()
            case 'schedule_update':
                self.schedule_update_valid()
            case 'anons_update':
                self.anons_update_valid()
            case 'series':
                self.schedule_valid()
            case 'series_update':
                self.series_update_valid()
            case 'delete_series':
                self.delete_series_valid()
        return action

    def schedule_valid(self):
        if Anime.objects.filter(anons=False).count() >= 1:
            raise forms.ValidationError('Данные уже записаны!')

    def anons_valid(self):
        if Anime.objects.filter(anons=True).count() >= 5:
            raise forms.ValidationError('Данные уже записаны!')

    def delete_valid(self):
        if not Anime.objects.count():
            raise forms.ValidationError('Данных для удаления нет!')

    def schedule_update_valid(self):
        if not Anime.objects.count():
            raise forms.ValidationError('Нет Данных для обновления!')

    def anons_update_valid(self):
        if not Anime.objects.filter(anons=True).count():
            raise forms.ValidationError('Нет Данных для обновления!')

    def series_valid(self):
        if Series.objects.count() >= 1:
            raise forms.ValidationError('Данные серий уже записаны!')

    def series_update_valid(self):
        if not Series.objects.count():
            raise forms.ValidationError('Данных для обновления нет!')

    def delete_series_valid(self):
        if not Series.objects.count():
            raise forms.ValidationError('Данных для удаления нет!')