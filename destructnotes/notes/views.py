from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return HttpResponse("<h1>Welcome to notes's page: Home page</h1>")

def about(request):
  return HttpResponse("<h1>Welcome to notes's page: About page</h1>")

def contact(request):
  return HttpResponse("<h1>Welcome to notes's page: Contact page</h1>")