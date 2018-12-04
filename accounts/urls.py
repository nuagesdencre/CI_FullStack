from django.urls import path, include
from .views import register, user_login, user_logout

urlpatterns = [
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('accounts/', include('django.contrib.auth.urls')),

]
