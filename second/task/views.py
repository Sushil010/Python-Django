from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    return render(request,'index.html')

def task_list(request):
    task=Task.objects.all().order_by('-created_at')
    return render(request,'task_list.html',{'task':task})
