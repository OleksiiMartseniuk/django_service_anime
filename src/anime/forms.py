from django import forms
from .models import Anime


class ParserForm(forms.Form):
    action = forms.ChoiceField(label='', widget=forms.Select, choices=[
        ('schedule', 'Запись аниме расписания'),
        ('anons', 'Запись аниме анонсов'),
        ('delete', 'Удаления всех записей и кеша'),
        ('schedule_update', 'Обновить аниме расписания'),
        ('anons_update', 'Обновить аниме анонсов'),
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
        return action

    def schedule_valid(self):
        if Anime.objects.count() >= 1:
            raise forms.ValidationError('Данные уже записаны!')

    def anons_valid(self):
        if Anime.objects.filter(anons=True).count() >= 5:
            raise forms.ValidationError('Данные уже записаны!')

    def delete_valid(self):
        if not Anime.objects.count():
            raise forms.ValidationError('Данных для удаления нет!')