from django.shortcuts import render

from .models import Project
def index(request):
    return render(request, 'projects.html')

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'projects.html' , context)

def project(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {'projects': projects}
    return render(request, 'projects.html' , context)

