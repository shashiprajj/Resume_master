from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Poem, Poem_Images
from .forms import PostCreateForm, PostUpdateForm
from django.forms import modelformset_factory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.


class PoemListView(LoginRequiredMixin, ListView):
    model = Poem
    template_name = "poems/all_poems.html"
    context_object_name = "all_poems"
    ordering = ['-date_posted']


class User_Poems(LoginRequiredMixin, ListView):
    model = Poem
    template_name = "poems/user_poems.html"
    context_object_name = "user_poems"
    ordering = ["-date_posted"]
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Poem.objects.filter(username=user).order_by("-date_posted")


@login_required(login_url='/login/')
def create_poems(request):
    modelformset = modelformset_factory(
        Poem_Images, fields=("poem_image", ), extra=5)
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        formset = modelformset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            poem = form.save(commit=False)
            poem.username = request.user
            poem.save()

            for f in formset:
                try:
                    photo = Poem_Images(
                        poem=poem, poem_image=f.cleaned_data["poem_image"])
                    photo.save()
                except Exception as e:
                    break
            return redirect("all_poems")

    else:
        form = PostCreateForm()
        formset = modelformset(queryset=Poem_Images.objects.none())
    return render(request, "poems/create_poems.html", {"form": form, "formset": formset})


@login_required(login_url='/login/')
def poem_update(request, pk):
    post = get_object_or_404(Poem, id=pk)
    modelformset = modelformset_factory(
        Poem_Images, fields=("poem_image", ), extra=3)

    if post.username != request.user:
        raise Http404()
    if request.method == "POST":
        form = PostUpdateForm(request.POST or None, instance=post)
        formset = modelformset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            form.save()
            data = Poem_Images.objects.filter(poem=post)

            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        photo = Poem_Images(
                            poem=post, poem_image=f.cleaned_data.get("poem_image"))
                        photo.save()
                    elif f.cleaned_data["poem_image"] is False:
                        photo = Poem_Images.objects.get(
                            id=request.POST.get('form-' + str(index) + '-id'))
                        photo.delete()
                    else:
                        photo = Poem_Images(
                            poem=post, poem_image=f.cleaned_data.get("poem_image"))
                        d = Poem_Images.objects.get(id=data[index].id)
                        d.poem_image = photo.poem_image
                        d.save()

            return redirect("all_poems")
    else:
        form = PostUpdateForm(instance=post)
        formset = modelformset(queryset=Poem_Images.objects.filter(poem=post))

    context = {
        'form': form,
        'post': post,
        'formset': formset
    }
    return render(request, "poems/poem_update.html", context)


class PoemDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Poem
    template_name = "poems/poem_delete.html"
    success_url = "/all_poems/"
    context_object_name = "poem"

    def test_func(self):
        poem = self.get_object()
        if self.request.user == poem.username:
            return True
        else:
            return False


class PoemDetailView(LoginRequiredMixin, DetailView):
    model = Poem
    template_name = "poems/poem_detail.html"
    context_object_name = "poem"
