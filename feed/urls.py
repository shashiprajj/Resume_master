from django.urls import path
from . import views
from .views import FeedListView, FeedDetailView, PostDelete, UserPostListView

urlpatterns = [
    path("all_posts/", FeedListView.as_view(), name="all_posts"),
    path("posts_detail/<int:pk>/detail",
         views.FeedDetailView, name="posts_detail"),
    path("user_posts/<str:username>/",
         UserPostListView.as_view(), name="user_posts"),
    path("likes/", views.like_post, name="like_post"),
    path("post_create/", views.Post_Create, name="post_create"),
    path("post_update/<int:pk>/update", views.post_update, name="post_update"),
    path("post_delete/<int:pk>/delete", PostDelete.as_view(), name="post_delete"),
]
