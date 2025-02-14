from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request,'index.html')

def task_field(request):
    task=Task.objects.all().order_by('-created_at')
    return render(request,'task_page.html',{'task':task})

