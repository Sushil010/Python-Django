from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Notes

# Create your views here.
def forms(request):
    if request.method=="POST":
        datas=request.POST.get("tasks")
        Notes.objects.create(text=datas)

        all_data=Notes.objects.all()

        return render(request,'td/task_list.html',{'dat':all_data})
    return render(request,"td/form.html")
