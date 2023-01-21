from django import forms

from src.base import messages

from .models import Anime, Series, ScreenImages


class ParserForm(forms.Form):
    action = forms.ChoiceField(label='', widget=forms.Select, choices=[
        ('schedule', messages.SCHEDULE_FORM),
        ('anons', messages.ANONS_FORM),
        ('delete', messages.DElETE_SCHEDULE_FORM),
        ('delete_img', messages.DELETE_IMG_FILE_FORM),
        ('schedule_update', messages.SCHEDULE_UPDATE_FORM),
        ('anons_update', messages.ANONS_UPDATE_FORM),
        ('series', messages.SERIES_FORM),
        ('series_update', messages.SERIES_UPDATE_FORM),
        ('delete_series', messages.DElETE_SERIES_FORM),
        ('update_indefinite_exit', messages.UPDATE_INDEFINITE_EXIT),
        ('write_telegram', messages.WRITE_TELEGRAM_BOT_FORM),
        ('full_update', messages.FULL_UPDATE),
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
            case 'delete_img':
                self.delete_img_valid()
            case 'schedule_update':
                self.schedule_update_valid()
            case 'anons_update':
                self.anons_update_valid()
            case 'series':
                self.series_valid()
            case 'series_update':
                self.series_update_valid()
            case 'delete_series':
                self.delete_series_valid()
            case 'write_telegram':
                self.write_telegram_valid()
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

    def delete_img_valid(self):
        if Anime.objects.count() and ScreenImages.objects.count():
            raise forms.ValidationError('Данные в бд не удалены!')

    def write_telegram_valid(self):
        if not Anime.objects.filter(telegram_id_file=None).count():
            raise forms.ValidationError('Нет данных для записи')
