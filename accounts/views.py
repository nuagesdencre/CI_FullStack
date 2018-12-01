from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfile, UserForm
from django.contrib.auth import authenticate, login, logout



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

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfile(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            # OneToOne relationship

            if 'profile_img' in request.FILES:
                profile.profile_img = request.FILES['profile_img']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfile()
    return render(request, 'register.html',
                  {'user_form': user_form, "profile_form": profile_form, "registered": registered})


def user_login(request):
    """
    Display the the login page and verify an inputted
     username and password combination
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You are now logged in')
                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                messages.error(request,"This account is not active.")
                return render(request, "login.html")
        else:
            messages.error(request,"Invalid login details provided.")
            return render(request, "login.html")
    else:
        args = {'next': request.GET.get('next', '')}
        return render(request, 'login.html', args)

@login_required
def user_logout(request):
    """
    Log the user out and redirect back to the index page
    """
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect(reverse('index'))


def profile(request):
    """
    Display the profile page of a user
    """
    return render(request, 'profile.html')



