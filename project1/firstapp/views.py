from django.shortcuts import render
from .models import Aeroplane
from django.shortcuts import get_object_or_404
from .forms import AeroVarietyForm

# Create your views here.

def first_app(request):
    aeroplane=Aeroplane.objects.all()
    return render(request,'firstapp/firstapp.html',{'aeroplane':aeroplane})

def aero_desc(request,aero_id):
    aero_det=get_object_or_404(Aeroplane,pk=aero_id)
    return render(request,'firstapp/aero_desc.html',{'aero_det':aero_det})
    

def aer_variety(request):
    stores=None
    if request.method=='POST':
        form=AeroVarietyForm(request.POST)
        if form.is_valid():
            aero_variety = form.cleaned_data['aero_variety']

    return render(request,'firstapp/aer_variety.html',{'stores':stores})
