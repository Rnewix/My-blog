from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name= 'index'


urlpatterns = [
    path('', views.index, name='home')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



