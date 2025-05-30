from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    return render(request,"users/index.html")
    # return HttpResponse("welecome to the page")


def login_method(request):
    if request.method=="POST":
        pass

def logout_method(request):
    if request.method=="POST":
        pass