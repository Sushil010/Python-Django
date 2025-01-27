from django.shortcuts import render

# Create your views here.

def first_app(request):
    return render(request,'firstapp/first_app.html')

