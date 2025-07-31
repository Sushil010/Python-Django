from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import blog
from django.contrib import messages

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
            messages.success(request,"Blog created successfully")
            return redirect("main",
                    #   {'title':title,
                    #     'content':content
                    #     }
                        )
        else:
            messages.warning(request,"Both fields are required")
        

    # return HttpResponse("Start creating")
    return render(request,"blog/create.html")
    # if request.method="POST":


def delete_posts(request,idx):
    posts=get_object_or_404(blog,id=idx)
    posts.delete()
    messages.info(request,"Blog deleted")
    return redirect("main")

def edit_posts(request,idx):
    editable=get_object_or_404(blog,id=idx)
    if request.method=="POST":
        new_text_title=request.POST.get("ed_title")
        new_text_content=request.POST.get("ed_content")

        editable.title=new_text_title
        editable.content=new_text_content
        editable.save()

        return redirect("main")

    return render(request,"blog/edit.html",{
        'values':editable
        })