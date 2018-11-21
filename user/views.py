from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


def user(request):
    """
    Display the main page of the User app
    """
    return render(request, 'user.html')


def register(request):
    """
    Display the registration form
    """
    return render(request, 'register.html')


def login(request):
    """
    Display the the login form
    """
    return render(request, 'login.html')


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




