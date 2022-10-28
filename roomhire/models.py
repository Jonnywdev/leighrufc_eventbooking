from django.db import models


class RoomHire(models.Model):

    class Meta:
        verbose_name_plural = 'Room Hire Request'

    full_name = models.CharField(max_length=300)
    email_address = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11)
    event_type = models.CharField(max_length=80, null=True)
    date_of_event = models.DateField()
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    num_people = models.CharField(max_length=20)
    other_details = models.TextField(blank=True)

    def __str__(self):
        return self.event_type
