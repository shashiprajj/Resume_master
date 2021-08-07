from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "username"]


# @admin.register(Poem)
# class PoemAdmin(admin.ModelAdmin):
#     list_display = ["id", "username", "poem_name"]


# @admin.register(Certificate)
# class CertificateAdmin(admin.ModelAdmin):
#     list_display = ["id", "username", "course_name"]


# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ["id", "username", "project_title"]
