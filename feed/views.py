from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Feed, Feed_Image
from .forms import FeedForm, FeedUpdateForm
from django.forms import modelformset_factory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# Create your views here.


class UserPostListView(LoginRequiredMixin, ListView):
    model = Feed
    template_name = "feed/user_posts.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Feed.objects.filter(username=user).order_by("-date_posted")


class FeedListView(LoginRequiredMixin, ListView):
    model = Feed
    template_name = "feed/all_posts.html"
    context_object_name = "posts"
    ordering = ['-date_posted']


@login_required(login_url='/login/')
def FeedDetailView(request, pk):
    post = Feed.objects.get(pk=pk)
    total_likes = post.total_likes()

    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    return render(request, "feed/posts_detail.html", {"post": post, "is_liked": is_liked, "total_likes": total_likes})


@login_required(login_url='/login/')
def like_post(request):
    post = get_object_or_404(Feed, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    context = {
        "post": post,
        "is_liked": is_liked,
        "total_likes": post.total_likes()
    }
    if request.is_ajax():
        html = render_to_string('feed/like_section.html',
                                context, request=request)
        return JsonResponse({"form": html})


@login_required(login_url='/login/')
def Post_Create(request):
    modelformset = modelformset_factory(
        Feed_Image, fields=("feed_image", ), extra=5)
    if request.method == "POST":
        form = FeedForm(request.POST)
        formset = modelformset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            feed = form.save(commit=False)
            feed.username = request.user
            feed.save()

            for f in formset:
                try:
                    photo = Feed_Image(
                        feed=feed, feed_image=f.cleaned_data["feed_image"])
                    photo.save()
                except Exception as e:
                    break

            return redirect("all_posts")
    else:
        form = FeedForm()
        formset = modelformset(queryset=Feed_Image.objects.none())
    return render(request, "feed/create_feed.html", {"form": form, "formset": formset})


@login_required(login_url='/login/')
def post_update(request, pk):
    post = get_object_or_404(Feed, id=pk)
    modelformset = modelformset_factory(
        Feed_Image, fields=("feed_image", ), extra=3)
    if request.method == "POST":
        form = FeedUpdateForm(request.POST or None, instance=post)
        formset = modelformset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            form.save()
            data = Feed_Image.objects.filter(feed=post)

            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        photo = Feed_Image(
                            feed=post, feed_image=f.cleaned_data["feed_image"])
                        photo.save()
                    elif f.cleaned_data["feed_image"] is False:
                        photo = Feed_Image.objects.get(
                            id=request.POST.get('form-' + str(index) + '-id'))
                        photo.delete()
                    else:
                        photo = Feed_Image(
                            feed=post, feed_image=f.cleaned_data["feed_image"])
                        d = Feed_Image.objects.get(id=data[index].id)
                        d.feed_image = photo.feed_image
                        d.save()

        return HttpResponseRedirect(post.get_absolute_url())

    else:
        form = FeedUpdateForm(instance=post)
        formset = modelformset(queryset=Feed_Image.objects.filter(feed=post))

    context = {
        "form": form,
        "formset": formset
    }
    return render(request, "feed/post_update.html", context)


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Feed
    template_name = "feed/post_delete.html"
    success_url = "/all_posts/"
    context_object_name = "post"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return False
