from django.shortcuts import render


def index(request):
    """
    Return the INDEX (home) page of Creature Comforts
    (this is the welcome page of the app)
    """
    return render(request, 'index.html')


def contact(request):
    """
    Return the CONTACT page of Creature Comforts
    """
    return render(request, "contact.html")


def about(request):
    """
    Return the ABOUT page of Creature Comforts
    """
    return render(request, 'about.html')


def faqs(request):
    """
    Return the FAQs page of Creature Comforts
    """
    return render(request, 'faq.html')
