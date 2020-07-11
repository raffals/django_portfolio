# from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project, SlideShowProject, Slide

def project_list(request):
    # Remember double folder structure in templates dir = need to pre-pend projects/ to template file
    return render(request, 'projects/index.html')


def all_projects(request):
    # Query the db to return all project objects
    projects = Project.objects.all()
    slide_projects = SlideShowProject.objects.all()
    # print(projects)
    # Above command prints to console:
    # <QuerySet [<Project: Project object (1)>, <Project: Project object (2)>, <Project: Project object (3)>]>
    #
    # Remember double folder structure in templates dir = need to pre-pend projects/ to template file
    return render(request, 'projects/all_projects.html', {'projects': projects, 'slide_projects': slide_projects})

def project_detail(request, pk):
    # Query the db to return project id=pk object
    project = Project.objects.get(pk=pk)
    #print(project)
    return render(request, 'projects/project_detail.html', {'project': project})

def slide_project_detail(request, pk):
    # Query the db to return project id=pk object
    project = SlideShowProject.objects.get(pk=pk)
    print(project)
    return render(request, 'projects/slide_project_detail.html', {'project': project})

def project_slides(request, pk):
    # Query the db to return project id=pk object
    project = SlideShowProject.objects.get(pk=pk)
    # Return just the slides for this project
    slides = Slide.objects.filter(project=pk)
    return render(request, 'projects/project_slides.html', {'project': project, 'slides': slides})
