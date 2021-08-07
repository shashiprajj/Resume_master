from django.urls import path
from .views import (CertificateDelete, CertificateDetailView, CertificateListView, CertificatePost,
                    CertificateUpdate, CourseraPostListView, EdxPostListView, UdemyPostListView, OthersPostListView,
                    DrawingPostListView, SportsPostListView)
from . import views

urlpatterns = [
    path("all_certificates/", CertificateListView.as_view(),
         name="all_certificates"),
    path("course_detail/<int:pk>/",
         CertificateDetailView.as_view(), name="course_detail"),
    path("post_certificate/new/", CertificatePost.as_view(),
         name="post_certificate"),
    path("certificate/<int:pk>/update/",
         CertificateUpdate.as_view(), name="update_certificate"),
    path("certificate/<int:pk>/delete",
         CertificateDelete.as_view(), name="delete_certificate"),
    path("coursera/<str:username>/",
         CourseraPostListView.as_view(), name="coursera"),
    path("edx/<str:username>/", EdxPostListView.as_view(), name="edx"),
    path("udemy/<str:username>/", UdemyPostListView.as_view(), name="udemy"),
    path("drawing/<str:username>/", DrawingPostListView.as_view(), name="drawing"),
    path("sports/<str:username>/", SportsPostListView.as_view(), name="sports"),
    path("others/<str:username>/", OthersPostListView.as_view(), name="others"),
]
