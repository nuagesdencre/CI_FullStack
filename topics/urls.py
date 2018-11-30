from django.urls import path
from . import views

app_name = 'topics'
urlpatterns = [
    path('', views.ListTopics.as_view(), name='all'),
    path('new', views.CreateTopic.as_view(), name='create'),
    path('posts/in/<topic_name>', views.SingleTopic.as_view(), name='single'),
    path('follow/<topic_name>', views.FollowTopic.as_view(), name='follow'),
    path('unfollow/<topic_name>', views.UnfollowTopic.as_view(), name='unfollow'),
]
