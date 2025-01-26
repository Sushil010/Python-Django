from django.http import HttpResponse

def Home(request):
    return HttpResponse('Hello, World!')

def About(request):
    return HttpResponse("From about section")

def contacts(request):
    return HttpResponse("Contact informations!!!")