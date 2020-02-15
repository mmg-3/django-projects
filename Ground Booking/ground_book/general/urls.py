from django.conf.urls import url
from . import views

app_name = 'general'

urlpatterns = [
    url(r'^gallery/$', views.GalleryView.as_view(), name='gallery'),
    url(r'^events/$', views.AvailableEvents.as_view(), name='available_events'),
    url(r"^events/in/(?P<slug>[-\w]+)/$", views.SingleEvent.as_view(), name="single"),
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^contact/$', views.Contact.as_view(), name='contact'),
]
