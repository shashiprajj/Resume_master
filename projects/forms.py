from django import forms
from .models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["project_title", "project_description",
                  "project_code_link", "project_website_link", "date_posted"]

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["project_title", "project_description",
                  "project_code_link", "project_website_link", "date_posted"]