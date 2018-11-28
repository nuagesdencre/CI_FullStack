from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # EXTEND USER ATTRIBUTES BY EXTENDING THE USER CLASS
    user = models.OneToOneField(User, on_delete = models.DO_NOTHING)
    # COMMUNITY PAGE
    twitter_handle = models.CharField(max_length=100, blank=True)
    community_page = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_imgs', blank=True)

    def __str__(self):
        return self.user.username