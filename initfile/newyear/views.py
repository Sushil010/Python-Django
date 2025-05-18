from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def newresponse(request):
    now=datetime.datetime.now()
    return render(request,"new/inidex.html",{
        'newyear':now.month==5 and now.day==18
    })