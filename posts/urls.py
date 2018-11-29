from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new', views.CreatePost.as_view(), name='create'),
    path('auth/<username>', views.UserPosts.as_view(), name='for_user'),
    path('auth/<username>/<pk>', views.PostDetail.as_view(), name='single'),
    path('delete/<pk>', views.DeletePost.as_view(), name='delete'),
]
