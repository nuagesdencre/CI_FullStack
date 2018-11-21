from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    """
    Where visitors who have gone through registration can log in
    """
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    """
    Where visitors can register to access user-specific features of the website
    """

    class Meta:
        model = User
        fields = ['email', 'username', 'psw', 'check_psw']
