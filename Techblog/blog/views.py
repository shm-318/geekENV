from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import *


# Create your views here.
def HomeView(request):
    return render(request,'socialapp_auth/auth_user.html',{})

def register(request):
    return render(request,'blog/register.html',{})


def IndexView(request):
    #if request.user.is_authenticated:
            #return redirect('/')
    return render(request,'blog/index.html',{})

def lead(request):
    return render(request,'blog/lead.html')

def Signout(request):
    logout(request)
    return redirect('index_view')

def contact(request):
    form1 = ContactForm()

    if request.method == 'POST':
        form1 = ContactForm(request.POST)

        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request, 'blog/contact.html', context={'form1': form1})

def about(request):
    return render(request, 'blog/about.html')


