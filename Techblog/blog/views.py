from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import View
from .models import *
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
    )
from django.contrib.auth import (
                                    authenticate, 
                                    login, 
                                    logout, 
                                    get_user_model,
                                )
from django.contrib import messages
from django.urls import reverse_lazy

User = get_user_model()

# Create your views here.
class ProfileView(View):
    template_name_auth = 'authentication/auth_user.html'
    template_name_anon = 'authentication/anon_user.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('<h1>This User does not exist.</h1>')

        
        if username == request.user.username:
            context = { 'user': user }
            return render(request, self.template_name_auth, context=context)
        else:
            context = { 'user': user }
            return render(request, self.template_name_anon, context=context)
        


def Signin(request, *args, **kwargs):

    if request.method == 'POST':
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')
        
        try:
            user_obj = User.objects.get(username=email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username 
        user = authenticate(request, username=email_username, password=password)
            
        if user is None:
            messages.error(request, 'Invalid Login.', extra_tags="error")
            return redirect('blog:signin') 
        
        
        login(request, user)
        
        #messages.success(request, 'Thanks for Login.', extra_tags='success')
        return redirect('blog:profile_view',request.user.username)
    return render(request,'blog/login.html') 

def IndexView(request):
    if request.user.is_authenticated:
        return redirect('blog:profile_view',request.user.username)
    return render(request,'blog/lead.html')

def Signout(request):
    logout(request)
    return redirect('blog:index_view')

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

# def register(request):
    
#     return render(request, 'blog/register.html')
def register(request):
    email_unique=True
    password_match=True
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        Email = request.POST.get('mail')
        phonenumber = request.POST.get('phone')
        password = request.POST.get('password1')
        confirmPassword = request.POST.get('password2')
        gender = request.POST.get('gender')
        print("Full Name : ",fullname)
        print("User Name : ",username)
        print("Email Address: ",Email)
        print("Phone Number: ",phonenumber)
        print("Password : ",password)
        print("Confirm Password: ",confirmPassword)
        print("Gender: ",gender)
        if password == confirmPassword:
            if len(User.objects.filter(email=Email)) == 0:
                User.objects.create(full_name=fullname,username=username,email=Email,phone_number=phonenumber,password=password,gender=gender)
                print("Registered Successfully....")
                return HttpResponseRedirect('/signin')
            else:
                email_unique=False
                return render(request,"blog/register.html",{'email_unique':email_unique,'password_match':password_match})
        else:
            password_match=False
            print("Password and Confirm Password does not Match..")
            return render(request,"blog/register.html",{'email_unique':email_unique,'password_match':password_match})
    return render(request,"blog/register.html",{'email_unique':email_unique,'password_match':password_match})

# def login(request):
#     return render(request,'blog/login.html')

class PRView(PasswordResetView):
    email_template_name = 'authentication/password_reset_email.html'
    template_name = 'authentication/password_reset.html'
    success_url = reverse_lazy('blog:password_reset_done')

class PRConfirm(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('blog:password_reset_complete')

class PRDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'
    

class PRComplete(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'
    