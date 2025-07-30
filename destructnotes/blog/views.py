from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import blog

# Create your views here.
def main(request):
    vals=blog.objects.all()
    return render(request,"blog/homepage.html",{"vals":vals})


def create_post(request):
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")
        if title.strip() and content.strip():
            blog.objects.create(title=title,content=content)
        return redirect("main",
                    #   {'title':title,
                    #     'content':content
                    #     }
                        )

    # return HttpResponse("Start creating")
    return render(request,"blog/create.html")
    # if request.method="POST":
