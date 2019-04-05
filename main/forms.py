from django import forms
from .models import Reminder


class InputForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Buy coffee Monday 23, 10am', 'autofocus': 'true', 'autocomplete': 'off'}), label='')

    class Meta:
        model = Reminder
        fields = ('body',)
