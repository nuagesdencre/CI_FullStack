from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile


class UserForm(forms.ModelForm):
    """
    Form through which visitors can register their details to access user-specific
    features of the website
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class UserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("community_page", "twitter_handle", "profile_image")

