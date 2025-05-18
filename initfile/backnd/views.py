from django.shortcuts import render
from django.http import HttpResponse
# from . import home

# Create your views here.
def index(request):
    return render(request,"home/index.html")

# def custom_names(request,name):
#     return HttpResponse(f"Hello {name}")

def custom_greet(request,name):
    return render(request,"home/index.html",{
        "name":name.capitalize()
    })