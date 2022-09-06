from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name= 'about_us'

urlpatterns = [
    path('', views.about_us, name='about_us')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)