from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms

class NewTaskForms(forms.Form):
    text=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",max_value=10,min_value=0)

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the task page")

todos=['get','play','pass']
def tasks(request):
    return render(request,"folders/index.html",{
        'todos':todos
    })

def add_tasks(request):
    return render(request,"folders/add.html",{
        "form":NewTaskForms()
    })
    # if request.method=="POST":
    #     tasks=request.POST.get("task")
    #     if tasks:
    #         todos.append(tasks)
    #     return redirect('add_tasks')
    # return render(request,"folders/add.html")
    # return redirect('todos')