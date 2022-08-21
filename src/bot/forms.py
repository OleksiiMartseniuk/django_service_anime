from django import forms

from src.base import messages


class BotForm(forms.Form):
    action = forms.ChoiceField(label='', widget=forms.Select, choices=[
        ('upload', messages.UPLOAD_BOT_FORM),
    ])
