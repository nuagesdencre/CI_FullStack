from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import Topic


class CreateTopic(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Topic


class SingleTopic(generic.DetailView):
    model = Topic


class ListTopics(generic.ListView):
    model = Topic
