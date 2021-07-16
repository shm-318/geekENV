
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    #url(r'^$',views.IndexView,name='index_view'),
    url(r'^$',views.lead,name='lead'),
    path('home/',views.HomeView,name="home_blog_view"),
    url(r'^contact/',views.contact,name="contact"),
    url(r'^about/',views.about,name="about"),
    url(r'^register/',views.register,name="register"),
    path('signout/', views.Signout, name='signout_view'),
]