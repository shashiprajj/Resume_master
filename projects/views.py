from django.shortcuts import render
from .models import Project, Project_Image
from django.forms import modelformset_factory
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import ProjectCreateForm, ProjectUpdateForm
# Create your views here.


class User_Projects(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/user_projects.html"
    context_object_name = "user_projects"
    ordering = ["-date_posted"]
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Project.objects.filter(username=user).order_by("-date_posted")


@login_required(login_url='/login/')
def create_projects(request):
    modelformset = modelformset_factory(
        Project_Image, fields=("project_image", ), extra=5)
    if request.method == "POST":
        form = ProjectCreateForm(request.POST)
        formset = modelformset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            project = form.save(commit=False)
            project.username = request.user
            project.save()

            for f in formset:
                try:
                    photo = Project_Image(
                        project=project, project_image=f.cleaned_data["project_image"])
                    photo.save()
                except Exception as e:
                    break
            return redirect("/user_projects/")

    else:
        form = ProjectCreateForm()
        formset = modelformset(queryset=Project_Image.objects.none())
    return render(request, "projects/create_projects.html", {"form": form, "formset": formset})


@login_required(login_url='/login/')
def project_update(request, pk):
    post = get_object_or_404(Project, id=pk)
    modelformset = modelformset_factory(
        Project_Image, fields=("project_image", ), extra=3)

    if post.username != request.user:
        raise Http404()
    if request.method == "POST":
        form = ProjectUpdateForm(request.POST or None, instance=post)
        formset = modelformset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            form.save()
            data = Project_Image.objects.filter(project=post)

            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        photo = Project_Image(
                            project=post, project_image=f.cleaned_data.get("project_image"))
                        photo.save()
                    elif f.cleaned_data["project_image"] is False:
                        photo = Project_Image.objects.get(
                            id=request.POST.get('form-' + str(index) + '-id'))
                        photo.delete()
                    else:
                        photo = Project_Image(
                            project=post, project_image=f.cleaned_data.get("project_image"))
                        d = Project_Image.objects.get(id=data[index].id)
                        d.project_image = photo.project_image
                        d.save()

            return redirect("user_projects")
    else:
        form = ProjectUpdateForm(instance=post)
        formset = modelformset(
            queryset=Project_Image.objects.filter(project=post))

    context = {
        'form': form,
        'post': post,
        'formset': formset
    }
    return render(request, "projects/project_update.html", context)


class ProjectDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "projects/project_delete.html"
    success_url = "/user_projects/"
    context_object_name = "project"

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.username:
            return True
        else:
            return False


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"
