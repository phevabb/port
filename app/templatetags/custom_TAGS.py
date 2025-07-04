from django import template
register = template.Library()
from django.shortcuts import render

from app.models import Project

# shop search form (ALL GET REQUESTS FORM the form comes here)
# post requests will be worked on somewhere

@register.simple_tag
def get_all_projects():
    return Project.objects.all()