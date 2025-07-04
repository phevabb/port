from django.shortcuts import render

from app.models import Project


# Create your views here.
def index(request):
    return render(request, 'index.html')


def detail(request, id=id):
    project = Project.objects.get(id=id)
    context = {'project': project}
    return render(request, 'detail.html', context=context)