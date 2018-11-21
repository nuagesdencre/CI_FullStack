from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    """
    Where visitors who have gone through registration can log in
    """
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    