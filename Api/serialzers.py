from django.db.models import fields
from rest_framework import serializers

from Api.models import PreBooking

class PreBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreBooking
        fields = '__all__'