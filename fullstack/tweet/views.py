from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm


# Create your views here.
def index(request):
    return render(request,'index.html')


def tweet_lists(request):
    tweet=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweet':tweet})

def tweet_submit(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)
        # if file is also being accepted use request.FILES in above
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})
