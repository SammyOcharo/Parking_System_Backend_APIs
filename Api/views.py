from django.shortcuts import render

from rest_framework.response import Response
from rest_framework .decorators import api_view

from .serialzers import PreBookingSerializer
from .models import PreBooking
# Create your views here.

@api_view(['GET'])
def List_display(request):
    All_Bookings = PreBooking.objects.all()
    serializer = PreBookingSerializer(All_Bookings, many=True)


    return Response(serializer.data)

@api_view(['POST'])
def createParkingSpot(request):

    serializer = PreBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)