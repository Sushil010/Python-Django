from django.shortcuts import render
from django.http import HttpResponse
from .models import blog

# Create your views here.
def main(request):
    return render(request,"blog/homepage.html")


def create_post(request):
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")
        if title.strip() and content.strip():
            blog.objects.create(title=title)
            blog.objects.create(content=content)
        vals=blog.objects.all()
        return render(request,"blog/homepage.html",
                    #   {'title':title,
                    #     'content':content
                    #     }
                    {'vals':vals}
                        )

    # return HttpResponse("Start creating")
    return render(request,"blog/homepage.html")
    # if request.method="POST":
