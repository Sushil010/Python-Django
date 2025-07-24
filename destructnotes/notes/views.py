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
            "time_stamp":time_stamp
        }

        # return render(request,)

    return render(request, "notes/form.html")






























# def about(request):
# #   return HttpResponse("<h1>Welcome to notes's page: About page</h1>")
#     return render(request,"notes/about.html")

# def contact(request):
# #   return HttpResponse("<h1>Welcome to notes's page: Contact page</h1>")
#     return render(request,"notes/contact.html")