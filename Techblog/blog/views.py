from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout


# Create your views here.
def HomeView(request):
    return render(request,'socialapp_auth/auth_user.html',{})


def IndexView(request):
    if request.user.is_authenticated:
            return redirect('home_blog_view')
    return render(request,'blog/index.html',{})

def Signout(request):
    logout(request)
    return redirect('index_view')