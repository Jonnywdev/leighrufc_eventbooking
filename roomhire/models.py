from django.db import models
from django.contrib.auth.models import User


class RequestForm(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    event_type = models.CharField(max_length=300)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_desc = models.TextField()
    entertainer = models.BooleanField(null=True, blank=True)
    food = models.BooleanField(null=True, blank=True)
    member = models.BooleanField(null=True, blank=True)
