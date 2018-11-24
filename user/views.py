from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, RegistrationForm



def user(request):
    """
    Display the main page of the User app
    """
    return render(request, 'user.html')


def register(request):
    """
    Display the registration form
    """
    registration_form = RegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})


def login(request):
    """
    Display the the login form
    """
    login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def logout(request):
    """
    Log the user out and redirect back to the index page
    """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


@login_required
def profile(request):
    """
    Display the profile page of a user (logged in)
    """
    return render(request, 'profile.html')




