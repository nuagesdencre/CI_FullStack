from django.urls import path
from .views import accounts, register, login, logout, profile

urlpatterns = [
    path('', accounts, name='accounts'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile'),
]
