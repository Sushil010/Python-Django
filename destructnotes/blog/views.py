from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import blog
from django.contrib import messages
from .forms import BlogForm

# Create your views here.

def main(request):
    query = request.GET.get('q')
    
    if query:
        vals = blog.objects.filter(title__icontains=query) | blog.objects.filter(content__icontains=query)
        blogs = vals  # for the upper loop
    else:
        vals = blog.objects.all()
        blogs = []  # to show 'no blog found' only when searching

    total_posts = vals.count()

    return render(request, "blog/homepage.html", {
        "vals": vals,
        "total_posts": total_posts,
        "blogs": blogs
    })

# def main(request):
#     vals=blog.objects.all()
#     total_posts=vals.count()

#     return render(request,"blog/homepage.html",{
#         "vals":vals,
#         "total_posts":total_posts
#         })


def create_post(request):
    if request.method=="POST":
        
        # title=request.POST.get("title")
        # content=request.POST.get("content")
        form=BlogForm(request.POST)
        
        
        # if title.strip() and content.strip():
        #     blog.objects.create(title=title,content=content)
        if form.is_valid():
            form.save()
            messages.success(request,"Blog created successfully")
            return redirect("main",
                    #   {'title':title,
                    #     'content':content
                    #     }
                        )
        else:
            messages.warning(request,"Correct the errors")
    else:
        form=BlogForm()
    # return HttpResponse("Start creating")
    return render(request,"blog/create.html",{"form":form})
    # if request.method="POST":


def delete_posts(request,idx):
    posts=get_object_or_404(blog,id=idx)
    posts.delete()
    messages.info(request,"Blog deleted")
    return redirect("main")

def edit_posts(request,idx):
    editable=get_object_or_404(blog,id=idx)
    if request.method=="POST":
        
        # new_text_title=request.POST.get("ed_title")
        # new_text_content=request.POST.get("ed_content")
        
        form=BlogForm(request.POST,instance=editable)
        
        # editable.title=new_text_title
        # editable.content=new_text_content
        # editable.save()
        # return redirect("main")
        
        if form.is_valid():
            form.save()
            messages.success("Blog successfully edited")
            return redirect("main")
        else:
            messages.warning(request,"Correct the errors below")
    else:
        form=BlogForm(instance=editable)
       
    return render(request,"blog/edit.html",{"form":form})
    # return render(request,"blog/edit.html",{
    #     'values':editable
    #     })


def search(request):
    query=request.GET.get('q')
    if query:
        blogs = blog.objects.filter(title__icontains=query) | blog.objects.filter(content__icontains=query)

    else:
        blogs=blog.objects.all()
    
    return render(request,"blog/homepage.html",{"blog":blogs})