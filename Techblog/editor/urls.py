from django.urls import path
from editor.views import home,postdetail,uploadi,uploadf,upload_link_view,editpost
from django.views.decorators.csrf import csrf_exempt 

from django.conf.urls.static import static
from django.conf import settings

app_name='editor'
urlpatterns = [
    path('',home ),
    path('<int:id>/',postdetail ),
    path('editpost/<int:id>/',editpost ),
    path('uploadi/',csrf_exempt(uploadi) ),
    path('uploadf/',csrf_exempt(uploadf) ),
    path('linkfetching/',upload_link_view),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)