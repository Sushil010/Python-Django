from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "notes/form.html")

# def about(request):
# #   return HttpResponse("<h1>Welcome to notes's page: About page</h1>")
#     return render(request,"notes/about.html")

# def contact(request):
# #   return HttpResponse("<h1>Welcome to notes's page: Contact page</h1>")
#     return render(request,"notes/contact.html")