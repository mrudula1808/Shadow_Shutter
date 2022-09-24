from django.db import models

class Photographer(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    photographer=models.ForeignKey(Photographer,on_delete=models.SET_NULL,null=True,blank=True)
    image =models.ImageField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)

    def __str__(self):
        return self.description


class Bookings(models.Model):
    name=models.CharField(blank=False, max_length=30)
    email=models.EmailField(blank=False, max_length=50)
    address=models.TextField(blank=False, max_length=200)
    photographer=models.CharField(blank=False,max_length=30)
    booking_date=models.DateField(blank=False,)
    booking_time=models.TimeField(blank=False)
    booking_hours=models.CharField(blank=False,max_length=2)