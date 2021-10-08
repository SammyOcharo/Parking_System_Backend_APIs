from django.contrib import admin
from .models import PreBooking

class PreBookingAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Location', 'Parking_Slot', 'Parking_Date')

# Register your models here.
admin.site.register(PreBooking, PreBookingAdmin)