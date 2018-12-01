from django.urls import path
from . import views

app_name = 'topics'
urlpatterns = [
    path('', views.ListTopics.as_view(), name='all'),
    path('new', views.CreateTopic.as_view(), name='create'),
    path('posts/in/<slug>', views.SingleTopic.as_view(), name='single'),
    path('follow/<slug>', views.FollowTopic.as_view(), name='follow'),
    path('unfollow/<slug>', views.UnfollowTopic.as_view(), name='unfollow'),
]
