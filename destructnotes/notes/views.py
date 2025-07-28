from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Notes 
import uuid
import datetime

# Create your views here.
# note_Store={}
# def note_form(request):
#     if request.method=="POST":
#         content=request.POST.get("note")
#         note_id=str(uuid.uuid4())
#         time_stamp=datetime.datetime.now()

#         note_Store[note_id]={
#             "content":content,
#             "time_stamp":time_stamp,
#             "viewed":False
#         }

#         return render(request,"notes/share_url.html",{"note_id":note_id})

#     return render(request, "notes/form.html")


def note_form(request):
    
    if request.method=="POST":
        content=request.POST.get("note") ##note is a variable stored in form 
        note=Notes.objects.create(content=content)
       
        
        return redirect('show_notes')

        # return render(request,"notes/share_url.html",{"note_id":note.note_id})
    return render(request,"notes/form.html")




def view_note(request,note_id):
    note=get_object_or_404(Notes,note_id=note_id)
    

    now=datetime.datetime.now(datetime.timezone.utc)
    if (now-note.created_at).total_seconds()>300 or note.viewed==True:
        return HttpResponse("Note has expired")
    
    note.viewed=True
    note.save()
    return HttpResponse(f"{note.content}")
    # note=note_Store.get(note_id)
       
        # # note={
        # # "content": "hello world",
        # # "time_stamp": datetime.datetime(2025, 7, 23, 22, 15),
        # # "viewed": False
        # # }
    
    # if not note:
    #     return HttpResponse("Note not found")
    
    # now=datetime.datetime.now()
    # diff=(now-note['time_stamp']).total_seconds()
    # if note["viewed"]==True or diff>300:
    #     return HttpResponse("Note has expired")
        
    # note["viewed"]=True
    # return HttpResponse(f"Note:{note['content']}")





def show_notes(request):
    if request.method=="POST":
        content=request.POST.get('note')
        Notes.objects.create(content=content)

        notes=Notes.objects.all().order_by('-created_at')
        return render(request,"notes/index.html",{"notes":notes})

























# def about(request):
# #   return HttpResponse("<h1>Welcome to notes's page: About page</h1>")
#     return render(request,"notes/about.html")

# def contact(request):
# #   return HttpResponse("<h1>Welcome to notes's page: Contact page</h1>")
#     return render(request,"notes/contact.html")