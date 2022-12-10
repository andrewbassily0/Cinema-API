from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    room = models.CharField(max_length=30)

class Guest(models.Model):
    name =models.CharField(max_length=30)
    age = models.IntegerField()
    mobile = models.CharField(max_length=40)
    address = models.CharField(max_length=100)

class Reservation(models.Model):
    Movies =models.ForeignKey(Movies, related_name='reservation' , on_delete=models.CASCADE)
    Guest =models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE)
    date = models.DateField()

    