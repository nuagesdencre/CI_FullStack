from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def user(request):
    """
    Display the main page of the User app
    """
    return render(request, 'user.html')


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
                return redirect(reverse('user'))
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
        login_form = AuthenticationForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                messages.error(None, "Your username or password is incorrect")
    else:
        login_form = AuthenticationForm()
    args = {'login_form': login_form, 'next': request.GET.get('next', '')}
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




