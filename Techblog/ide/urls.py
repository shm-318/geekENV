from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'ide'
urlpatterns = [
    path('',views.index),
    #url(r'^run/$', views.runCode, name='run'),
    path('run/',views.runCode,name='runide'),
]
