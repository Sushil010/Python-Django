from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def forms(request):
    if request.method=="post":
        pass
    # return render(request,"td/form.html")