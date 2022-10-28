from django.forms import ModelForm
from django import forms
from .models import RoomHire


class RoomHireForm(ModelForm):
    class Meta:
        model = RoomHire
        fields = ('full_name', 'email_address', 'phone_number', 'event_type',
                  'date_of_event', 'start_time', 'end_time',
                  'num_people', 'other_details')
        labels = {
            'full_name': 'Full Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'event_type': 'Type of Event e.g. 50th Birthday Party',
            'date_of_event': 'What date do you want to book the room out?',
            'start_time': 'What time do you want it to start?',
            'end_time': 'What time do you want it to end?',
            'num_people': 'How many people will be attending (MAX: 100)',
            'other_details': 'Any other details'
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'event_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'date_of_event': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'yyyy/mm/dd'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'From 11am - 7pm'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'From 12pm - 12am'}),
            'num_people': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'other_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
        }
