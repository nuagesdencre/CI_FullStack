from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

User = get_user_model()


# TOPIC
class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")
    description_html = models.TextField(editable=False, blank=True, default="")
    # many to many relationship
    followers = models.ManyToManyField(User, through="TopicFollower")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class TopicFollower(models.Model):
    topic = models.ForeignKey(Topic, related_name="followings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("topic", "user")
