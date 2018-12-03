from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def index(request):
    """
    Return the index page of the home app
    (this is the welcome page of the app)
    """
    return render(request, 'index.html')


def contact(request):
    """
    Return the contact page of the home app
    """
    return render(request, "contact.html")


def about(request):
    """
    Return the about page of the home app
    """
    return render(request, 'about.html')


def faqs(request):
    """
    Return the FAQs page of the home app
    """
    faqs = {'Fact_1': 'This is a test.', 'Fact_2': 'This is a test too.',
            'Fact_3': 'This is also a test.'}
    return render(request, 'faq.html', context=faqs)
