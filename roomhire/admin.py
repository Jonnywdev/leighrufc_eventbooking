from django.contrib import admin
from .models import RoomHire


# Register your models here.
@admin.register(RoomHire)
class RoomHireAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'event_type', 'date_of_event')
    ordering = ('date_of_event', )
    search_fields = ('full_name', 'event_type', 'date_of_event')
