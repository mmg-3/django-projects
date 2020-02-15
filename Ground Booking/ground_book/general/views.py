from django.views.generic import (TemplateView, DetailView)
from .models import Gallery, AvailEvents
from django.shortcuts import render
# Create your views here.


class GalleryView(TemplateView):
    model = Gallery
    template_name = 'general/gallery.html'

    def get(self, request):
        gallery = Gallery.objects.all()
        context = {'gallery': gallery}
        return render(request, self.template_name, context)


class AvailableEvents(TemplateView):
    template_name = 'general/available_events.html'
    model = AvailEvents

    def get(self, request):
        events = AvailEvents.objects.all()
        context = {'events': events}
        return render(request, self.template_name, context)


class SingleEvent(DetailView):
    model = AvailEvents
    template_name = 'general/single_event.html'


class About(TemplateView):
    template_name = 'general/about.html'


class Contact(TemplateView):
    template_name = 'general/contact.html'

