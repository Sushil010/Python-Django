from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms

class NewTaskForms(forms.Form):
    text=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",max_value=8,min_value=0)

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the task page")

todos=['get','play','pass']
def tasks(request):
    return render(request,"folders/index.html",{
        'todos':todos
    })

def add_tasks(request):
    if request.method=="POST":
        # task=NewTaskForms() this command will just create a new blank form and to 
        # populate the data we are gonna use request.POST this is sort of like
        # filling or getting data into the task variable
        form=NewTaskForms(request.POST)
        if form.is_valid():
            # from.cleaned_data will be used to retreive all user data 
            # Similarly form.cleaned_data["task"] will get only the task field
            task=form.cleaned_data["text"]
            todos.append(task)
        else:
            return render(request,"folders/add.html",{
                "form":form
            })

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