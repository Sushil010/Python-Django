from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def main_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login')) 
    
    # this_line--->invokes=urls.py=goes_to_login_name-->that_login_redirects_to
    # views.login_method_below-->now_that_method_invokes_index.htm_file inside_of
    # users_folder. 

    # return render(request,"users/index.html")
    # return HttpResponse("welecome to the page")


def login_method(request):
    return render(request,'users/index.html')
    # if request.method=="POST":
    #     pass

def logout_method(request):
    if request.method=="POST":
        pass