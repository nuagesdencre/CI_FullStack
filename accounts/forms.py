from django import forms
from django.contrib.auth.models import User
from accounts.models import ProfileModel


class UserForm(forms.ModelForm):
    """
    Form through which visitors can register their details to access user-specific
    features of the website
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserProfile(forms.ModelForm):
    profile_img = forms.ImageField(label="Profile Image")
    class Meta:
        model = ProfileModel
        fields = ("community_page", "twitter_handle", "profile_img")

