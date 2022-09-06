from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)