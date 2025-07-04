from django.shortcuts import render

from app.models import Project


# Create your views here.
# views.py
from django.db.models.functions import Lower

def index(request):
    projects = Project.objects.all().order_by(Lower('title'))
    return render(request, 'index.html', {'projects': projects})


def detail(request, id=id):
    project = Project.objects.get(id=id)
    context = {'project': project}
    return render(request, 'detail.html', context=context)