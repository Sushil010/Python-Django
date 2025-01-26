from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse('Hello, World!')
    return render(request,'website/index.html')

def About(request):
    # return HttpResponse("From about section")
    return render(request,'website/about.html')

def contacts(request):
    # return HttpResponse("Contact informations!!!")
    return render(request,'website/contact.html')