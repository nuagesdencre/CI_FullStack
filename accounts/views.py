from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def accounts(request):
    """
    Display the main page of the Accounts app
    """
    return render(request, 'accounts.html')


def register(request):
    """
    Display the registration form
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('accounts'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = RegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})


def login(request):
    """
    Display the the login page and verify an inputted
     username and password combination
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        authentication_form = AuthenticationForm(request.POST)

        if authentication_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in")

            if user:
                    auth.login(user=user, request=request)
            else:
                authentication_form.add_error(None, "Your username or password is incorrect")
    else:
        authentication_form = AuthenticationForm()
    args = {'authentication_form': authentication_form}
    return render(request, "login.html", args)


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




