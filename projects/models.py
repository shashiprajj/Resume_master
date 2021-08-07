from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, models.CASCADE)
    project_title = models.CharField(max_length=100)
    project_description = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    project_code_link = models.CharField(
        max_length=200, default="None", null=True, blank=True)
    project_website_link = models.CharField(
        max_length=200, default="None", null=True, blank=True)

    def __str__(self):
        return self.project_title

class Project_Image(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_image = models.ImageField(
        upload_to="project_image/", blank=True, null=True)

    def __str__(self):
        return self.project.project_title