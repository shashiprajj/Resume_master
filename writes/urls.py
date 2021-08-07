from django.urls import path
from . import views
from .views import PoemDelete, PoemDetailView, User_Poems, PoemListView

urlpatterns = [
    path("all_poems/", PoemListView.as_view(), name="all_poems"),
    path("user_poems/", User_Poems.as_view(), name="user_poems"),
    path("create_poems/", views.create_poems, name="create_poems"),
    path("poem_update/<int:pk>/update", views.poem_update, name="poem_update"),
    path("poem_delete/<int:pk>/delete", PoemDelete.as_view(), name="poem_delete"),
    path("poem_detail/<int:pk>/", PoemDetailView.as_view(), name="poem_detail"),
]
