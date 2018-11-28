from django.urls import path, include
from .views import accounts, register, user_login, user_logout, profile

urlpatterns = [
    path('', accounts, name='accounts'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('profile', profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),

]
