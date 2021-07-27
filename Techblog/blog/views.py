from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import View
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
        
        """ try:
            user_obj = User.objects.get(username=email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username """
        user = authenticate(request, username=email_username, password=password)
            
        if user is None:
            messages.error(request, 'Invalid Login.', extra_tags="error")
            return redirect('blog:index_view') 
        
        
        login(request, user)
        
        #messages.success(request, 'Thanks for Login.', extra_tags='success')
        return redirect('blog:profile_view',request.user.username)


def IndexView(request):
    if request.user.is_authenticated:
        return redirect('blog:profile_view',request.user.username)
<<<<<<< HEAD
    return render(request,'blog/lead.html',{})
=======
    return render(request,'blog/index.html',{})
>>>>>>> 4fd2b35cfc5da738bf4731bd3910fe7ff1bdf2ff

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

def register(request):
    return render(request, 'blog/register.html')


class PRView(PasswordResetView):
    email_template_name = 'authentication/password_reset_email.html'
    template_name = 'authentication/password_reset.html'
    success_url = reverse_lazy('blog:password_reset_done')

class PRConfirm(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('blog:password_reset_complete')

class PRDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'
    

<<<<<<< HEAD
=======
class PRView(PasswordResetView):
    email_template_name = 'authentication/password_reset_email.html'
    template_name = 'authentication/password_reset.html'
    success_url = reverse_lazy('blog:password_reset_done')

class PRConfirm(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('blog:password_reset_complete')

class PRDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'
    

>>>>>>> 4fd2b35cfc5da738bf4731bd3910fe7ff1bdf2ff
class PRComplete(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'
    