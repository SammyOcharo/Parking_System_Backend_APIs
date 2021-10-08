from django.urls import path

from . import views

urlpatterns = [
    path('display/',views.List_display, name='display'),
    path('get-parking/',views.createParkingSpot, name='get-parking'),
]