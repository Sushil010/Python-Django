from django.db import models

# Create your models here.
class Flights(models.Model):
    origin = models.CharField(max_length=62)
    destination=models.CharField(max_length=62)
    duration=models.IntegerField()