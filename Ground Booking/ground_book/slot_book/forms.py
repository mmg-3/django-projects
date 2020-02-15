from django import forms
from .models import BookingDetails


class BookingForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'email', 'team_name', 'contact', 'slot_date', 'slot_num')
        model = BookingDetails
