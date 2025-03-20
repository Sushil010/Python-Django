from django.shortcuts import render
from .models import TodoItems
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404,redirect
from .forms import TodoForm, UserRegistrationForm


# Create your views here.
 

def task(request):
    return render(request,'index.html')



def todos(request):
    if request.method=='POST':
        form=TodoForm(request.POST,request.FILES)
        if form.is_valid():
            tasks=form.save(commit=False)
            tasks.user=request.user
            tasks.save()
            return redirect("todos")
    
        else:
            form=TodoForm()
    return render(request,'todos.html',{'form':form})

    # if request.method=='POST':
    #     title=request.POST.get('title')
    #     TodoItems.objects.create(title=title, completed=False) 
    #     return redirect("todos") 

    # items=TodoItems.objects.all()
    # return render(request,'todos.html',{'items':items})



def deletetodo(request,todos_id):
    task=get_object_or_404(TodoItems,pk=todos_id,user=request.user)
    if request.method=='POST':
        task.delete()
        return redirect('todos')
    return render(request,'todos.html',{'tasks':task})

    # task=get_object_or_404(TodoItems,pk=todos_id)
    # if request.method=='POST':
    #     task.delete()
    #     return redirect('todos')
    
    # return render(request,'todos.html')
    