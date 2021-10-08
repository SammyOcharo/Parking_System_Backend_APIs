from django.db import models

# Create your models here.

class PreBooking (models.Model):
    Name= models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=13)
    Location = models.CharField(max_length=255)
    Parking_Slot = models.CharField(max_length=255)
    Parking_Date = models.DateTimeField()

    def __str__(self):
        return self.Name