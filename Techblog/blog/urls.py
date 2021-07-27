from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views
from .views import  PRView, PRDone, PRConfirm, PRComplete


app_name='blog'
urlpatterns = [
    url(r'^$',views.IndexView,name='index_view'),
    path('home/<str:username>/',views.ProfileView.as_view(),name="profile_view"),
    url(r'^contact/',views.contact,name="contact"),
    url(r'^about/',views.about,name="about"),
<<<<<<< HEAD
    url(r'^register/',views.register,name="register"),
=======
>>>>>>> 4fd2b35cfc5da738bf4731bd3910fe7ff1bdf2ff
    path('signout/', views.Signout, name='signout'),
    path('signin/', views.Signin, name='signin'),


    #password reset
    path('password/reset/', PRView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>', PRConfirm.as_view() , name='password_reset_confirm'),
    path('password/reset/done/',  PRDone.as_view() ,name='password_reset_done'),
    path('password/reset/complete/', PRComplete.as_view() , name='password_reset_complete'),

    
]