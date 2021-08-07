from django.contrib import admin
from .models import Project, Project_Image
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "project_title"]

@admin.register(Project_Image)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ["id", "project", "project_image"]