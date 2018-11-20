from django.shortcuts import render


def index(request):
    """
    Return the index page of the home app
    (this is the welcome page of the app)
    """
    return render(request, 'index.html')
