from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'john.doe'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Super secret'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            if not User.objects.filter(username=username).exists():
                raise forms.ValidationError('This user does not exist')
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Incorrect Password')

        return super(LoginForm, self).clean(*args, **kwargs)


class SignUpForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'john@example.com'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'john.doe'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Super secret'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'A user with that email already exists.')

        return email
