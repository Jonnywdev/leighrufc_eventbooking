from django.forms import ModelForm
from django import forms
from .models import RequestForm


class EventRequest(ModelForm):
    full_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=11)
    event_type = forms.CharField(max_length=300)
    date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    event_desc = forms.CharField()
    entertainer = forms.BooleanField()
    food = forms.BooleanField()
    member = forms.BooleanField()

    class Meta:
        model = RequestForm
        fields = ['full_name', 'email', 'phone_number', 'event_type', 'date',
                  'start_time', 'end_time', 'event_desc', 'entertainer', 
                  'food', 'member']
