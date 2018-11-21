from django.urls import path
from .views import index, contact, about, faq

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('faq', faq, name='faq'),
]
