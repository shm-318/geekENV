from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views

app_name='blog'
urlpatterns = [
    url(r'^$',views.IndexView,name='index_view'),
    path('home/',views.HomeView,name="home_blog_view"),
    url(r'^contact/',views.contact,name="contact"),
    url(r'^about/',views.about,name="about"),
    path('signout/', views.Signout, name='signout_view'),
]