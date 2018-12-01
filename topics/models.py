from django.db import models
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
from django.utils.text import slugify
import misaka
User = get_user_model()
register = template.Library()

# TOPIC


class Topic(models.Model):
    name = models.CharField(max_length=155, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, max_length=255, default="")
    description_html = models.TextField(editable=False, blank=True, default="")
    # many to many relationship
    followers = models.ManyToManyField(User, through="TopicFollower")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("topics:single", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]


class TopicFollower(models.Model):
    topic = models.ForeignKey(Topic, related_name="following", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ["topic", "user"]
