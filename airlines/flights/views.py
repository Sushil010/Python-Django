from django.shortcuts import render
from .models import Flights,Passangers
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        # get the flight with that flight id
        flight=Flights.objects.get(pk=flight_id)
        # the below line is to get the passanger id from the form
        passanger=Passangers.objects.get(pk=int(request.POST["passanger"]))
        # like adding a new row to the table
        passanger.flights.add(flight)
        return HttpResponseRedirect(reverse("get_details",args=(flight.id,)))