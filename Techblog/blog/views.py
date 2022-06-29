from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import View
from .models import *
from django.conf import settings
from django.contrib import messages
import requests

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


#! for confirmation mail
from .forms import UserForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
#from django.contrib.auth.models import User
from django.core.mail import EmailMessage, message, send_mail


User = get_user_model()

# for editor


def createBlog(request):
    return render(request, 'blog/editor.html', {})


# Signup user with email confirmation
def signup(request):
    if request.method == 'POST':
        print("enter in post")
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            print("enter at before mail")
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            # print(current_site.id)
            # for checking
            print(user, current_site.domain, urlsafe_base64_encode(
                force_bytes(user.pk)), account_activation_token.make_token(user))

            mail_subject = 'Activate your GeekENV account.'
            message = render_to_string('authentication/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            print("email sent")
            return render(request, 'authentication/aftersendlinktomail.html')
        else:
            print("form is not valid")
            form = UserForm(request.POST)
            return render(request, 'authentication/register_s.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'authentication/register_s.html', {'form': form})


# activate function used in signup view
def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('blog:signin')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# User Profile view
class ProfileView(View):
    template_name_auth = 'authentication/auth_user.html'
    template_name_anon = 'authentication/anon_user.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('<h1>This User does not exist.</h1>')

        # set picture_url

        if username == request.user.username:
            context = {'user': user}
            return render(request, self.template_name_auth, context=context)
        else:
            context = {'user': user}
            return render(request, self.template_name_anon, context=context)


# sign in
def Signin(request, *args, **kwargs):

    if request.method == 'POST':
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(username=email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username
        user = authenticate(
            request, username=email_username, password=password)

        if user is None:
            messages.error(request, 'Invalid Login.', extra_tags="error")
            return redirect('blog:signin')

        login(request, user)

        #messages.success(request, 'Thanks for Login.', extra_tags='success')
        return redirect('blog:blog_view', request.user.username)
    return render(request, 'blog/login.html')

# Main page


def IndexView(request):
    if request.user.is_authenticated:
        return redirect('blog:profile_view', request.user.username)
    response=requests.get('https://newsapi.org/v2/everything?q=programming&from=2022-01-05&sortBy=popularity&apiKey=cd0565836d8743369c48a336dc08e944').json()
    return render(request, 'blog/lead.html',{'response':response})
# signout


def Signout(request):
    logout(request)
    return redirect('blog:index_view')

# contact


def contact(request):
    form1 = ContactForm()

    if request.method == 'POST':
        form1 = ContactForm(request.POST)

        if form1.is_valid():
            form1.save()

            name = request.POST['Name']
            email = request.POST['Email']
            contact = request.POST['ContactNo']
            query = request.POST['Message']

            subject = f"Message from {name}"
            message = f"Hey There!\nA user named {name} Contacted us with the message:\n{query}\nContact details: {contact} \nEmail : {email} \n "
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_from, ]

            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Query Submitted Successfully')
            return redirect('/')
    return render(request, 'blog/contact.html', context={'form1': form1})

# about


def about(request):
    return render(request, 'blog/about.html')

# Resistration of new user with no confirmation mail


def register(request):
    email_unique = True
    password_match = True
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        Email = request.POST.get('mail')
        phonenumber = request.POST.get('phone')
        password = request.POST.get('password1')
        confirmPassword = request.POST.get('password2')
        gender = request.POST.get('gender')
        print("Full Name : ", fullname)
        print("User Name : ", username)
        print("Email Address: ", Email)
        print("Phone Number: ", phonenumber)
        print("Password : ", password)
        print("Confirm Password: ", confirmPassword)
        print("Gender: ", gender)
        if password == confirmPassword:
            if len(User.objects.filter(email=Email)) == 0:
                User.objects.create(full_name=fullname, username=username, email=Email,
                                    phone_number=phonenumber, password=password, gender=gender)
                print("Registered Successfully....")
                return HttpResponseRedirect('/signin')
            else:
                email_unique = False
                return render(request, "blog/register.html", {'email_unique': email_unique, 'password_match': password_match})
        else:
            password_match = False
            print("Password and Confirm Password does not Match..")
            return render(request, "blog/register.html", {'email_unique': email_unique, 'password_match': password_match})
    return render(request, "blog/register.html", {'email_unique': email_unique, 'password_match': password_match})

# forgot Password


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


# bot

def Yourbot(request):
    return render(request, 'authentication/bot.html')


# user blog view

class BlogView(View):
    template_name_auth = 'authentication/auth_blog.html'
    template_name_anon = 'authentication/anon_blog.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('<h1>This User blog does not exist.</h1>')

        if username == request.user.username:
            context = {'user': user}
            return render(request, self.template_name_auth, context=context)
        else:
            context = {'user': user}
            return render(request, self.template_name_anon, context=context)


# profile edit
class ProfileEditView(View):
    template_name = 'authentication/profile_edit.html'
    form_class = UserEditForm

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        if username != request.user.username:
            return HttpResponse('<h1>This page does not exist.</h1>')

        form = self.form_class(instance=request.user)
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Saved your details in a safe place.')
            return redirect('blog:profile_edit_view', request.user.username)
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            context = {'form': form}
            return render(request, self.template_name, context=context)
