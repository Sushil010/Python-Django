from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fir(request):
    return HttpResponse("Welcome to todos")