from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    username = models.OneToOneField(User)
    email = models.EmailField()
    team = models.CharField(max_length=50)
    phone = models.CharField(max_length=256, blank=True, null=True)
