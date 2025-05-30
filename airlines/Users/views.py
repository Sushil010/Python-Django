from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def main_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login')) 
    # return render(request,"users/index.html")
    # return HttpResponse("welecome to the page")


def login_method(request):
    return render(request,'users/index.html')
    # if request.method=="POST":
    #     pass

def logout_method(request):
    if request.method=="POST":
        pass