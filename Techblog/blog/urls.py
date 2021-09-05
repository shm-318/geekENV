from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from blog import views
from .views import  PRView, PRDone, PRConfirm, PRComplete
from ide.views import runCode

app_name='blog'
urlpatterns = [
    url(r'^$',views.IndexView,name='index_view'),
    #index page
    path('home/<str:username>/',views.ProfileView.as_view(),name="profile_view"),

    url(r'^contact/',views.contact,name="contact"),
    url(r'^about/',views.about,name="about"),
    
    url(r'^createblog/',views.createBlog,name="createblog"),

    #for signin/signout
    path('signout/', views.Signout, name='signout'),
    path('signin/', views.Signin, name='signin'),
    url(r'^register/',views.register,name="register"),
    #url(r'^login/',views.login,name="login"),
    
    #for email confirmation
    path('signup/', views.signup, name='signup'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),

    #password reset
    path('password/reset/', PRView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>', PRConfirm.as_view() , name='password_reset_confirm'),
    path('password/reset/done/',  PRDone.as_view() ,name='password_reset_done'),
    path('password/reset/complete/', PRComplete.as_view() , name='password_reset_complete'),

    #bot
    path('YourBot',views.Yourbot,name='Bot'),

    #ide
    path('ide',runCode,name='ideforyou')
]