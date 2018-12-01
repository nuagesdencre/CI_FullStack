from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from .models import Topic, TopicFollower


class CreateTopic(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Topic


class SingleTopic(generic.DetailView):
    model = Topic


class ListTopics(generic.ListView):
    model = Topic


class FollowTopic(generic.RedirectView, LoginRequiredMixin):
    """
    Allow a user to follow a topic
    """

    def get_redirect_url(self, *args, **kwargs):
        """
        Once an user follows a topic, he is returned to that topic's detailed view
        """
        return reverse('topics:single', kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        """
        Check if user is already a member; if yes, return an error message.
        Otherwise return a success message
        """
        topic = get_object_or_404(Topic, slug=self.kwargs.get('slug'))
        try:
            TopicFollower.objects.create(user=self.request.user, topic=topic)
        except:
            messages.warning(self.request, 'You already follow this Topic.')
        else:
            messages.success(self.request, 'You now follow this Topic.')
        return super().get(request, *args, **kwargs)


class UnfollowTopic(LoginRequiredMixin, generic.RedirectView):
    """
    Allow a user to unfollow a topic
    """

    def get_redirect_url(self, *args, **kwargs):
        return reverse('topics:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        """
        Check if user is actually following the topic he is trying to unfollow
        """
        try:
            following = TopicFollower.objects.filter(user=self.request.user,
                                                     topic__slug=self.kwargs.get('slug')).get()
        except TopicFollower.DoesNotExist:
            messages.warning(self.request, 'You do not follow this Topic.')
        else:
            following.delete()
            messages.success(self.request, 'You have stopped following this Topic.')
        return super().get(request, *args, **kwargs)
