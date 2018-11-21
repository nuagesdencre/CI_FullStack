from django.urls import path
from .views import user, register, login, logout, profile

urlpatterns = [
    path('', user, name='user'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile'),
]
