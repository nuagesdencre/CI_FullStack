from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import Topic, TopicFollower, Post

def blog(request):
    """
    Display the main blog page
    """
    return render(request, 'blog.html')
