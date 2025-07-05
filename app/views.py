from django.shortcuts import render, get_object_or_404

from app.models import Project


# Create your views here.
# views.py
from django.db.models.functions import Lower

def index(request):
    projects = Project.objects.all().order_by(Lower('title'))
    return render(request, 'index.html', {'projects': projects})


def detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tech_list = [tech.strip() for tech in project.tech_used.split(',')]
    return render(request, 'detail.html', {
        'project': project,
        'tech_list': tech_list,
    })


