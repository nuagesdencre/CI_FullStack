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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class UserProfile(forms.ModelForm):
    """
    Form through which visitors can provide optional information about themselves
    """
    class Meta:
        model = Profile
        fields = ["website", "twitter_handle", "profile_image"]


