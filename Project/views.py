from django.shortcuts import render
from .models import Project

# Create your views here.
def showProjects(request):
    projects = Project.objects.all()
    if request.method == "GET":
        return render(request, "showProjects.html", {"projects": projects})
    elif request.method == "POST":
        project = projects.filter()
        return render(request, "showProjects.html", {"projects": projects})
