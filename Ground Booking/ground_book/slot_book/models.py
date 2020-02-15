from django.db import models
from datetime import datetime, date
from django.urls import reverse


class BookingDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    team_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    slot_date = models.DateField('Slot Date(mm/dd/yyyy)', auto_now_add=False, auto_now=False)
    booked_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    slot_choices = (
                    ('1:6am-10am', '6am-10am'),
                    ('2:10am-2pm', '10am-2pm'),
                    ('3:2pm-5pm', '2pm-5pm'),
                    )
    slot_num = models.CharField(max_length=30, choices=slot_choices)

    def __str__(self):
        return self.name

    def save(self, *args):
        super().save(*args)

    def get_absolute_url(self):
        return reverse('booking:checkout')


