from django.shortcuts import render
from .models import Aeroplane

# Create your views here.

def first_app(request):
    aeroplane=Aeroplane.objects.all()
    return render(request,'firstapp/firstapp.html',{'aeroplane':aeroplane})

