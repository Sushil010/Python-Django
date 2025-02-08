from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect


# Create your views here.
def index(request):
    return render(request,'index.html')


def tweet_lists(request):
    tweet=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweet':tweet})

def tweet_create(request):
    if request.method=="POST":
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_lists')
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})



# def tweet_submit(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)
        # if file is also being accepted use request.FILES in above
        # Now check if the form is valid
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})


def tweet_edit(request,tweet_id):
    # to get tweet to edit for the user
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        # if the form is submitted with data then update the tweet with the new data and save it
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_lists')
    else:
        # the instance in the bracket is used to show the data in the form which is to be edited
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})


def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_lists')
    return render(request,'tweet_delete_confirm.html',{'tweet':tweet})
