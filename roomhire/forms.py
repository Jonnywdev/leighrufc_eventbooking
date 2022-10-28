from django.forms import ModelForm
from django import forms
from .models import RoomHire


class RoomHireForm(ModelForm):
    class Meta:
        model = RoomHire
        fields = ('full_name', 'email_address', 'phone_number', 'event_type',
                  'date_of_event', 'start_time', 'end_time',
                  'num_people', 'other_details')
