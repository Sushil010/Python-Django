from django.shortcuts import render
from .models import Aeroplane
from django.shortcuts import get_object_or_404

# Create your views here.

def first_app(request):
    aeroplane=Aeroplane.objects.all()
    return render(request,'firstapp/firstapp.html',{'aeroplane':aeroplane})

def aero_desc(request,aero_id):
    aero_det=get_object_or_404(Aeroplane,pk=aero_id)
    return render(request,'firstapp/aero_desc.html',{'aero_det':aero_det})
    

def pil_info(request):
    return render(request,'firstapp/pil_info.html')
