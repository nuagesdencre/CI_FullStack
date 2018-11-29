from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ListTopics.as_view(), name='all'),
    path('new', views.CreateTopic.as_view(), name='create'),
    path('posts/in/<topic_name>', views.SingleTopic.as_view(), name='single'),
]
