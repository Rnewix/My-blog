from django.urls import path
from .views import ProjectsListView
from django.conf import settings
from django.conf.urls.static import static


app_name= 'my_projects'

urlpatterns = [
    #path('', views.my_projects, name='my_projects')
    path('', ProjectsListView.as_view(), name= 'my_projects')          
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

