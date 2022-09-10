from django.shortcuts import render
from django.views.generic import ListView
from .models import Projects
# Create your views here.

       
class ProjectsListView(ListView):                                         
                model= Projects
                template_name= 'my_projects/my_projects.html'
                context_object_name= "proyect_list"
                
# def my_projects(request):
#     return render(request, 'my_projects/my_projects.html') 