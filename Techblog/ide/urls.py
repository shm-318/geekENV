from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'ide'
urlpatterns = [
    path('geekIDE/',views.Ide,name='ideurl'),
    url(r'^run/$', views.runCode, name='run'), 
      
]
