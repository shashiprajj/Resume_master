from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, StudentLoginForm, StudentPasswordChangeForm, ProfileUpdateForm, UserUpdateForm
from django.forms import modelformset_factory
from final_resume.models import Personal_Detail, Address
# Create your views here.


@login_required(login_url='/login/')
def home(request):
    if request.user.is_authenticated:
        prof = Profile.objects.filter(username=request.user).exists()
        if prof == True:
            profile = Profile.objects.get(username=request.user)
        else:
            profile = None

        personal_detail = Personal_Detail.objects.filter(
            username=request.user).exists()
        if personal_detail == True:
            personal_detail = Personal_Detail.objects.get(
                username=request.user)
        else:
            personal_detail = None

        add = Address.objects.filter(username=request.user).exists()
        if add == True:
            address = Address.objects.get(username=request.user)
        else:
            address = None

        context = {
            "profile": profile,
            "personal_detail": personal_detail,
            "address": address,
        }
        return render(request, 'home.html', context)
    else:
        return redirect("login")


@login_required(login_url='/login/')
def home_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been Updated!!!')
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'home_update.html', context)


class StudentRegistrationView(View):
    def get(self, request):
        form = StudentRegistrationForm()
        return render(request, "login_system/register.html", {"form": form})

    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Congratulations!!! Registered Successfully. Login Now")
            return redirect('login')
        return render(request, "login_system/register.html", {"form": form})


class StudentLoginView(LoginView):
    template_name = "login_system/login.html"
    authentication_form = StudentLoginForm
