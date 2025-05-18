from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requets):
    return HttpResponse("Hello World")

# def custom_names()