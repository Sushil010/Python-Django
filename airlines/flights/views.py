from django.shortcuts import render
from .models import Flights,Passangers

# Create your views here.
def flight(request):
    return render(request,"flights/index.html",{
        "flights":Flights.objects.all(),
    })

def getDetails(request,flight_id):
    flight=Flights.objects.get(pk=flight_id)
    return render(request,"flights/planes.html",{
        "flight":flight,
        "passangers":flight.passangers.all(),
        "non_passanger":Passangers.objects.exclude(flights=flight).all()

    })

def book_flight(request,flight_id):
    if request.method=="POST":
        pass