from django.urls import path
from . import views
from .views import User_Projects, ProjectDetailView, ProjectDelete

urlpatterns = [
    path("user_projects/", User_Projects.as_view(), name="user_projects"),
    path("project_detail/<int:pk>/",
         ProjectDetailView.as_view(), name="project_detail"),
    path("create_projects/", views.create_projects, name="create_projects"),
    path("project_update/<int:pk>/update",
         views.project_update, name="project_update"),
    path("project_delete/<int:pk>/delete",
         ProjectDelete.as_view(), name="project_delete"),

]
