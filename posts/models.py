from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from topics.models import TopicFollower, Topic
from django.urls import reverse

User = get_user_model()


# POST


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    content_html = models.TextField(editable=False, blank=True, default="")
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={"username":self.user.username, "pk":self.pf})

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("user", "content")