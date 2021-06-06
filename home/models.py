from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=122)
    Address = models.CharField(max_length=200)
    email = models.CharField(max_length=122)
    mobile_no = models.IntegerField()
    age = models.IntegerField()
    aadhar_no = models.IntegerField()
    source = models.CharField(max_length=122)
    destination = models.CharField(max_length=122)
    Seat = models.CharField(max_length=122)

    def __str__(self):
        return self.name