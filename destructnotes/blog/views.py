from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import blog

# Create your views here.
def main(request):
    vals=blog.objects.all()
    total_posts=vals.count()

    return render(request,"blog/homepage.html",{
        "vals":vals,
        "total_posts":total_posts
        })


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


def delete_posts(request,idx):
    posts=get_object_or_404(blog,id=idx)
    posts.delete()
    return redirect("main")

def edit_posts(request,idx):
    editable=get_object_or_404(blog,id=idx)
    # if request.method=="POST":
    #     editable.title=editable.

    return render(request,"blog/edit.html",{
        'values':editable
        })