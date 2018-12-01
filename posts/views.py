from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models
from topics.models import Topic

User = get_user_model()

class UserPosts(LoginRequiredMixin, generic.ListView, SelectRelatedMixin):
    """
    View the posts assigned to a specific user
    """
    model = models.Post
    template_name = 'posts/user_post_list.html'
    select_related = ('user', 'topic')
    queryset = models.Post.objects.all()

    def get_queryset(self):
        """
        Use the username details to retrieve related posts
        (while checking that the username does exist; if not, throw an error)
        """
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        """
        Populate a dictionary to use as the template context
        """
        context = super(UserPosts, self).get_context_data(**kwargs)
        context["post_user"] = self.post_user
        context['user_topics'] = Topic.objects.filter(followers__in=[self.request.user])
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    """
    Return detailed view of a single post
    """
    model = models.Post
    select_related = ("user", "topic")

    def get_queryset(self):
        """
        Get the queryset for the post and
        ensure the username is equal to the user's username
        """
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    """
    Create and edit a post
    """
    fields = ('content', 'topic')
    model = models.Post

    def form_valid(self, form):
        """
        Assign the post created to the user
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    """
    Delete a post
    """
    model = models.Post
    select_related = ("user", "topic")
    success_url = reverse_lazy("all")

    def get_queryset(self):
        """
        Get the queryset for the post and
        ensure the username is equal to the user's username
        """
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        """
        Confirm when post is successfully deleted
        """
        messages.success(self.request, "Your post has been deleted.")
        return super().delete(*args, **kwargs)
