from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Aeroplane(models.Model):
    SEAT_TYPE=[
        ('LT','LEFT'),
        ('MD','MIDDLE'),
        ('RT','RIGHT')
    ]

    name= models.CharField(max_length=100)
    image=models.ImageField(upload_to='pros/')
    added_time=models.DateTimeField(default=timezone.now)
    choices=models.CharField(max_length=2,choices=SEAT_TYPE)
    description=models.TextField(default='')

    
    def __str__(self):
        return self.name


# defining relationships:
class Aero_review(models.Model):
    aero=models.ForeignKey(Aeroplane,on_delete=models.CASCADE)
    