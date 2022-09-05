from django.shortcuts import render

# Create your views here.


def my_projects(request):
    return render(request, 'my_projects/my_projects.html') 