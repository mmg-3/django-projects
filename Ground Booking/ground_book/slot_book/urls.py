from django.conf.urls import url
from . import views


app_name = 'booking'

urlpatterns = [
    url(r'^$', views.BookingInfoView.as_view(), name='booking_info'),
    url(r'^checkout/$', views.Checkout.as_view(), name='checkout'),
    url(r'^booked/$', views.Booked.as_view(), name='booked'),
]
