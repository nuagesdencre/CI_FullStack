from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # EXTEND USER ATTRIBUTES BY EXTENDING THE USER CLASS
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter_handle = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_imgs', null=True, blank=True)

    def __str__(self):
        return self.user.username