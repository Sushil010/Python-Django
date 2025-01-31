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
# 1. One to Many Relationship
class Aero_review(models.Model):
    ratings=[
        ('1','one'),
        ('2','two'),
        ('3','three'),
        ('4','four'),
        ('5','five')
    ]
    aero=models.ForeignKey(Aeroplane,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.CharField(max_length=1,choices=ratings)
    comment=models.TextField()
    time_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} has reviewed {self.aero.name} with rating {self.rating}'
    
   
# 2. Many to Many Relationship
class Pilots(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    aeroplanes=models.ManyToManyField(Aeroplane,related_name='pilots')

    def __str__(self):
        return self.name


# 3. One to One Relationship
class Blackbox(models.Model):
    blackbox=models.OneToOneField(Aeroplane,on_delete=models.CASCADE,related_name='blackbox')
    black_id=models.CharField(max_length=100)
    created_date=models.DateTimeField(default=timezone.now)
    damage_date=models.DateTimeField()

    def __str__(self):
        return self.name.blackbox