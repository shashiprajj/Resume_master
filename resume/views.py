from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Certificate
from .import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.


class CertificateListView(LoginRequiredMixin, ListView):
    model = Certificate
    template_name = "certificates/all_certificates.html"
    context_object_name = "all_certificate"
    ordering = ["-date_posted"]
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Certificate.objects.filter(username=user).order_by("-date_posted")


class CertificateDetailView(LoginRequiredMixin, DetailView):
    model = Certificate
    template_name = "certificates/course_detail.html"
    context_object_name = "certificate"


class CertificatePost(LoginRequiredMixin, CreateView):
    model = Certificate
    fields = ["course_name", "course_platform",
              "course_img", "date_completed", "course_description"]
    template_name = "certificates/post_certificate.html"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class CertificateUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Certificate
    fields = ["course_name", "course_platform",
              "course_img", "date_completed", "course_description"]
    template_name = "certificates/update_certificate.html"
    # context_object_name = "certificate"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        certificate = self.get_object()
        if self.request.user == certificate.username:
            return True
        else:
            return False


class CertificateDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Certificate
    template_name = "certificates/delete_certificate.html"
    success_url = "/"
    context_object_name = "certificate"

    def test_func(self):
        certificate = self.get_object()
        if self.request.user == certificate.username:
            return True
        else:
            return False


class CourseraPostListView(LoginRequiredMixin, ListView):
    model = Certificate
    template_name = 'certificates/coursera.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'coursera'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Certificate.objects.filter(course_platform="COURSERA", username=user).order_by("-date_posted")


class EdxPostListView(LoginRequiredMixin, ListView):
    model = Certificate
    template_name = 'certificates/edx.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'edx'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Certificate.objects.filter(course_platform="EDX", username=user).order_by("-date_posted")


class UdemyPostListView(LoginRequiredMixin, ListView):
    model = Certificate
    template_name = 'certificates/udemy.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'udemy'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Certificate.objects.filter(course_platform="UDEMY", username=user).order_by("-date_posted")


class OthersPostListView(LoginRequiredMixin, ListView):
    model = Certificate
    template_name = 'certificates/others.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'others'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Certificate.objects.filter(course_platform="OTHERS", username=user).order_by("-date_posted")


class DrawingPostListView(LoginRequiredMixin, ListView):
    model = Certificate
    template_name = 'certificates/drawing.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'drawing'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Certificate.objects.filter(course_platform="DRAWING", username=user).order_by("-date_posted")


class SportsPostListView(LoginRequiredMixin, ListView):
    model = Certificate
    template_name = 'certificates/sports.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'sports'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Certificate.objects.filter(course_platform="SPORTS", username=user).order_by("-date_posted")
