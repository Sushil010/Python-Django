from django.db import models
from django.utils import timezone

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
