from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index),
    url(r'^run/$', views.runCode, name='run'),
]
