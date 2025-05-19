from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the task page")

todos=['get','play','pass']
def tasks(request):
    return render(request,"folders/index.html",{
        'todos':todos
    })