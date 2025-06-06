from django.db import models

# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}({self.code})"
    


class Flights(models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return (f"{self.id}. From {self.origin} to {self.destination } within {self.duration} minutes")
    
class Passangers(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    # flights=models.OneToOneField(Flights,blank=True,related_name="passangers")
    flights=models.ManyToManyField(Flights,blank=True,related_name="passangers")

    def __str__(self):
        return f"{self.first} {self.last} "