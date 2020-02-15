from django.shortcuts import render
from django.views.generic import (CreateView,
                                  TemplateView,
                                  ListView)
from .models import BookingDetails
import datetime


class BookingInfoView(CreateView):
    fields = ('name', 'email', 'team_name', 'contact', 'slot_date', 'slot_num')
    model = BookingDetails
    # template_name = 'slot_book/bookingdetails_form.html'

    def form_valid(self, form):
        return super().form_valid(form)


class Booked(ListView):
    model = BookingDetails
    template_name = 'slot_book/booked_slots.html'

    def get(self, request):
        today = datetime.datetime.now()
        slots = BookingDetails.objects.filter(slot_date__gte=today)
        context = {'slots': slots}
        return render(request, self.template_name, context)


class Checkout(TemplateView):
    template_name = 'slot_book/checkout.html'
