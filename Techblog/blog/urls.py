from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.IndexView,name='index_view'),
    url('home/',views.HomeView,name="home_blog_view"),
    path('signout/', views.Signout, name='signout_view'),
]