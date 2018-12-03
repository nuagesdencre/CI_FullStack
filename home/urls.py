from django.urls import path
from .views import index, contact, about, faqs

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('faqs', faqs, name='faqs'),
]
