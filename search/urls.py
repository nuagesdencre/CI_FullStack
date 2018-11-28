from django.urls import path
from .views import search_index

urlpatterns = [
    path('', search_index, name='search_index'),
]
