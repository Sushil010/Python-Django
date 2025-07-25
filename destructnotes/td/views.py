from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Notes

# Create your views here.
def forms(request):
    if request.method=="post":
        datas=request.POST.get("tasks")
        notes=Notes.objects.create(text=datas)

        return HttpResponse("Submitted Successfully!!")
    return render(request,"td/form.html")