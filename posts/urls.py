from django.urls import path
from . import views
app_name='posts'
urlpatterns = [

    path('new', views.CreatePost.as_view(), name='create'),
    path('auth/<username>', views.UserPosts.as_view(), name='user_posts'),
    path('auth/<username>/<pk>', views.PostDetail.as_view(), name='single'),
    path('delete/<pk>', views.DeletePost.as_view(), name='delete'),
]
