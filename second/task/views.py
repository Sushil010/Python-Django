from django.shortcuts import render
from .models import TodoItems

# Create your views here.
 

def task(request):
    return render(request,'index.html')


def todos(request):
    items=TodoItems.objects.all()
    return render(request,'todos.html',{'items':items})