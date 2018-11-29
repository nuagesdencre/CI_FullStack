from django.urls import path, include
from .views import blog
from . import views

urlpatterns = [
    path('', blog, name='blog'),


]
