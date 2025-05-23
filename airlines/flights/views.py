from django.shortcuts import render
from .models import Flights

# Create your views here.
def flight(request):
    return render(request,"flights/index.html",{
        "flights":Flights.objects.all()
    })