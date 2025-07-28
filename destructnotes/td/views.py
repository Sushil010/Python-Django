from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Notes

# Create your views here.
def forms(request):
    if request.method=="POST":
        datas=request.POST.get("tasks")
        if datas.strip():
                Notes.objects.create(text=datas)

    all_data=Notes.objects.all()

        # return render(request,'td/task_list.html',{'dat':all_data})
    return render(request,"td/form.html",{'dat':all_data})
    # return render(request,"td/form.html")


def delete_tasks(request,ids):
    to_be_deleted_note=get_object_or_404(Notes,id=ids)
    to_be_deleted_note.delete()
    return redirect("forms")

def edit_tasks(request,ids):
    to_be_updated=get_object_or_404(Notes,id=ids)# gather data.1

    if request.method=="POST":#unless edit button is pressed won't execute2.
        new_text=request.POST.get("edit_text")#4.....
        if new_text.strip():
            to_be_updated.text=new_text
            to_be_updated.save()
            return redirect("forms")
    
    return render(request,"td/edit.html",{'to_update':to_be_updated})#3.


def comp_tasks(request,ids):
    notes=get_object_or_404(Notes,id=ids)

    if request.method=="POST":
        notes.completed=not notes.completed
        notes.save()
        return redirect("forms")