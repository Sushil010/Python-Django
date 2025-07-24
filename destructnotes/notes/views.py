from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid
import datetime

# Create your views here.
note_Store={}
def note_form(request):
    if request.method=="POST":
        content=request.POST.get("note")
        note_id=str(uuid.uuid4())
        time_stamp=datetime.datetime.now()

        note_Store[note_id]={
            "content":content,
            "time_stamp":time_stamp,
            "viewed":False
        }

        return render(request,"notes/share_url.html",{"note_id":note_id})

    return render(request, "notes/form.html")


def view_note(request,note_id):
    note=note_Store.get(note_id)
    # note={
    # "content": "hello world",
    # "time_stamp": datetime.datetime(2025, 7, 23, 22, 15),
    # "viewed": False
    # }
    
    if not note:
        return HttpResponse("Note not found")
    
    now=datetime.datetime.now()
    diff=(now-note['time_stamp']).total_seconds()
    if note["viewed"]==True or diff>300:
        return HttpResponse("Note has expired")
        
    note["viewed"]=True
    return HttpResponse(f"Note:{note['content']}")





























# def about(request):
# #   return HttpResponse("<h1>Welcome to notes's page: About page</h1>")
#     return render(request,"notes/about.html")

# def contact(request):
# #   return HttpResponse("<h1>Welcome to notes's page: Contact page</h1>")
#     return render(request,"notes/contact.html")