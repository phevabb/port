from django.contrib import admin

# Register your models here.
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("tag", "title")
    search_fields = ("tag",)