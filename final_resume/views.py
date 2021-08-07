from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView
from .utils import render_to_pdf
from django.template.loader import get_template
from .forms import (AddressUpdateForm, Std_10Form, Std_12Form, First_YearForm, Second_YearForm, Third_YearForm, Fourth_YearForm,
                    Std_10UpdateForm, Std_12UpdateForm, First_YearUpdateForm, Second_YearUpdateForm, Third_YearUpdateForm,
                    Fourth_YearUpdateForm, PersonalDetailUpdateForm, AddressForm, TechnicalSkillsUpdateForm, InterestsUpdateForm,
                    PersonalDetailForm, AddressForm, TechnicalSkillsForm, InterestsForm)
from .models import Std_10, Std_12, Year_1, Year_2, Year_3, Year_4, Personal_Detail, Address, Technical_Skills, Interests
from student.models import Profile
from resume.models import Certificate
from projects.models import Project
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login/')
def post_resume(request):
    std_10 = Std_10.objects.filter(username=request.user).exists()
    std_12 = Std_12.objects.filter(username=request.user).exists()
    personal_detail = Personal_Detail.objects.filter(
        username=request.user).exists()
    technical_skills = Technical_Skills.objects.filter(
        username=request.user).exists()
    interests = Interests.objects.filter(
        username=request.user).exists()

    context = {
        "personal_detail": personal_detail,
        "technical_skills": technical_skills,
        "interests": interests,
        "std_10": std_10,
        "std_12": std_12,
    }

    messages.success(
        request, f'Your Data will be safe with us. Kindly Fill all the details for Better Resume!!!')
    return render(request, "final_resume/post_resume.html", context)


@login_required(login_url='/login/')
def already_exist(request):
    return render(request, "update_and_delete/already_exist.html")

# PERSONAL DETAIL CREATE, UPDATE AND DELETE


@login_required(login_url='/login/')
def personal_detail_form(request):
    if request.method == "POST":
        personal_detail_form = PersonalDetailForm(request.POST)
        address_form = AddressForm(request.POST)
        personal_detail = Personal_Detail.objects.filter(
            username=request.user).exists()
        address = Address.objects.filter(username=request.user).exists()
        if personal_detail == True and address == True:
            return redirect("/already_exist/")

        if personal_detail_form.is_valid() and address_form.is_valid():
            pdf = personal_detail_form.save(commit=False)
            af = address_form.save(commit=False)
            pdf.username = request.user
            af.username = request.user
            pdf.save()
            af.save()
            messages.success(
                request, f'Your Personal Details form has been Submitted Successfully!!!')
            return redirect("/std_10_form/")
    else:
        personal_detail_form = PersonalDetailForm()
        address_form = AddressForm()
    context = {
        "personal_detail_form": personal_detail_form,
        "address_form": address_form
    }
    return render(request, "final_resume/personal_details.html", context)


@login_required(login_url='/login/')
def personal_detail_update(request):
    if request.method == "POST":
        personal_form = PersonalDetailUpdateForm(
            request.POST, instance=request.user.personal_detail)
        address_form = AddressUpdateForm(
            request.POST, instance=request.user.address)
        if personal_form.is_valid() and address_form.is_valid():
            personal_form.save()
            address_form.save()
            messages.success(
                request, f'Your Personal Detail form has been Updated Successfully!!!')
        return redirect("/")
    else:
        personal_form = PersonalDetailUpdateForm(
            instance=request.user.personal_detail)
        address_form = AddressUpdateForm(instance=request.user.address)
    return render(request, "update_and_delete/personal_detail_update.html", {"personal_form": personal_form, "address_form": address_form})


@login_required(login_url='/login/')
def personal_detail_delete(request):
    pers = Personal_Detail.objects.filter(username=request.user).exists()
    addr = Address.objects.filter(username=request.user).exists()
    if pers == True and addr == True:
        per = Personal_Detail.objects.get(username=request.user)
        add = Address.objects.get(username=request.user)
        per.delete()
        add.delete()
        messages.success(
            request, f'Your Personal Detail form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")


# 10th STANDARD CREATE, UPDATE AND DELETE

@login_required(login_url='/login/')
def std_10_form(request):
    if request.method == "POST":
        std_10_form = Std_10Form(request.POST)
        user_10 = Std_10.objects.filter(username=request.user).exists()
        if user_10 == True:
            return redirect("/already_exist/")

        if std_10_form.is_valid():
            form_10 = std_10_form.save(commit=False)
            form_10.username = request.user
            form_10.save()
            messages.success(
                request, f'Your 10th Standard form has been Submitted Successfully!!!')
            return redirect("/std_12_form/")
    else:
        std_10_form = Std_10Form()
    context = {
        "std_10_form": std_10_form,
    }
    return render(request, "final_resume/std_10.html", context)


@login_required(login_url='/login/')
def std_10_update(request):
    if request.method == "POST":
        form = Std_10UpdateForm(request.POST, instance=request.user.std_10)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your 10th Standard form has been Updated Successfully!!!')
        return redirect("/")
    else:
        form = Std_10UpdateForm(instance=request.user.std_10)
    return render(request, "update_and_delete/std_10_update.html", {"form": form})


@login_required(login_url='/login/')
def std_10_delete(request):
    st_10 = Std_10.objects.filter(username=request.user).exists()
    if st_10 == True:
        std_10 = Std_10.objects.get(username=request.user)
        std_10.delete()
        messages.success(
            request, f'Your 10th Standard form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")

# 12th STANDARD CREATE, UPDATE AND DELETE


@login_required(login_url='/login/')
def std_12_form(request):
    if request.method == "POST":
        std_12_form = Std_12Form(request.POST)
        user_12 = Std_12.objects.filter(username=request.user).exists()
        if user_12 == True:
            return redirect("/already_exist/")

        if std_12_form.is_valid():
            form_12 = std_12_form.save(commit=False)
            form_12.username = request.user
            form_12.save()
            messages.success(
                request, f'Your 12th Standard form has been Submitted Successfully!!!')
            return redirect("/first_year_form/")
    else:
        std_12_form = Std_12Form()
    context = {
        "std_12_form": std_12_form,
    }
    return render(request, "final_resume/std_12.html", context)


@login_required(login_url='/login/')
def std_12_update(request):
    if request.method == "POST":
        form = Std_12UpdateForm(request.POST, instance=request.user.std_12)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your 12th Standard form has been Updated Successfully!!!')
        return redirect("/")
    else:
        form = Std_12UpdateForm(instance=request.user.std_12)
    return render(request, "update_and_delete/std_12_update.html", {"form": form})


@login_required(login_url='/login/')
def std_12_delete(request):
    st_12 = Std_12.objects.filter(username=request.user).exists()
    if st_12 == True:
        std_12 = Std_12.objects.get(username=request.user)
        std_12.delete()
        messages.success(
            request, f'Your 12th Standard form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")


@login_required(login_url='/login/')
def degree_details(request):
    year_1 = Year_1.objects.filter(username=request.user).exists()
    year_2 = Year_2.objects.filter(username=request.user).exists()
    year_3 = Year_3.objects.filter(username=request.user).exists()
    year_4 = Year_4.objects.filter(username=request.user).exists()

    context = {
        "year_1": year_1,
        "year_2": year_2,
        "year_3": year_3,
        "year_4": year_4,
    }
    return render(request, "final_resume/degree.html", context)


# FIRST YEAR CREATE, UPDATE AND DELETE
@login_required(login_url='/login/')
def first_year_form(request):
    if request.method == "POST":
        first_year_form = First_YearForm(request.POST)
        year_1 = Year_1.objects.filter(username=request.user).exists()
        if year_1 == True:
            return redirect("/already_exist/")

        if first_year_form.is_valid():
            form_first_year = first_year_form.save(commit=False)
            form_first_year.username = request.user
            form_first_year.save()
            messages.success(
                request, f'Your 1st Year form has been Submitted Successfully!!!')
            return redirect("/second_year_form/")
    else:
        first_year_form = First_YearForm()
    context = {
        "first_year_form": first_year_form,
    }
    return render(request, "final_resume/first_year.html", context)


@login_required(login_url='/login/')
def first_year_update(request):
    if request.method == "POST":
        form = First_YearUpdateForm(request.POST, instance=request.user.year_1)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your First Year form has been Updated Successfully!!!')
        return redirect("/")
    else:
        form = First_YearUpdateForm(instance=request.user.year_1)
    return render(request, "update_and_delete/first_year_update.html", {"form": form})


@login_required(login_url='/login/')
def first_year_delete(request):
    ye_1 = Year_1.objects.filter(username=request.user).exists()
    if ye_1 == True:
        year_1 = Year_1.objects.get(username=request.user)
        year_1.delete()
        messages.success(
            request, f'Your First Year form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")

# SECOND YEAR CREATE, UPDATE AND DELETE


@login_required(login_url='/login/')
def second_year_form(request):
    if request.method == "POST":
        second_year_form = Second_YearForm(request.POST)
        year_2 = Year_2.objects.filter(username=request.user).exists()
        if year_2 == True:
            return redirect("/already_exist/")

        if second_year_form.is_valid():
            form_second_year = second_year_form.save(commit=False)
            form_second_year.username = request.user
            form_second_year.save()
            messages.success(
                request, f'Your 2nd Year form has been Submitted Successfully!!!')
            return redirect("/third_year_form/")
    else:
        second_year_form = Second_YearForm()
    context = {
        "second_year_form": second_year_form,
    }
    return render(request, "final_resume/second_year.html", context)


@login_required(login_url='/login/')
def second_year_update(request):
    if request.method == "POST":
        form = Second_YearUpdateForm(
            request.POST, instance=request.user.year_2)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your Second Year form has been Updated Successfully!!!')
        return redirect("/")
    else:
        form = Second_YearUpdateForm(instance=request.user.year_2)
    return render(request, "update_and_delete/second_year_update.html", {"form": form})


@login_required(login_url='/login/')
def second_year_delete(request):
    ye_2 = Year_2.objects.filter(username=request.user).exists()
    if ye_2 == True:
        year_2 = Year_2.objects.get(username=request.user)
        year_2.delete()
        messages.success(
            request, f'Your Second Year form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")

# THIRD YEAR CREATE, UPDATE AND DELETE


@login_required(login_url='/login/')
def third_year_form(request):
    if request.method == "POST":
        third_year_form = Third_YearForm(request.POST)
        year_3 = Year_3.objects.filter(username=request.user).exists()
        if year_3 == True:
            return redirect("/already_exist/")

        if third_year_form.is_valid():
            form_third_year = third_year_form.save(commit=False)
            form_third_year.username = request.user
            form_third_year.save()
            messages.success(
                request, f'Your 3rd Year form has been Submitted Successfully!!!')
            return redirect("/fourth_year_form/")
    else:
        third_year_form = Third_YearForm()
    context = {
        "third_year_form": third_year_form,
    }
    return render(request, "final_resume/third_year.html", context)


@login_required(login_url='/login/')
def third_year_update(request):
    if request.method == "POST":
        form = Third_YearUpdateForm(request.POST, instance=request.user.year_3)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your Third Year form has been Updated Successfully!!!')
        return redirect("/")
    else:
        form = Third_YearUpdateForm(instance=request.user.year_3)
    return render(request, "update_and_delete/third_year_update.html", {"form": form})


@login_required(login_url='/login/')
def third_year_delete(request):
    ye_3 = Year_3.objects.filter(username=request.user).exists()
    if ye_3 == True:
        year_3 = Year_3.objects.get(username=request.user)
        year_3.delete()
        messages.success(
            request, f'Your Third Year form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")

# FOURTH YEAR CREATE, UPDATE AND DELETE


@login_required(login_url='/login/')
def fourth_year_form(request):
    if request.method == "POST":
        fourth_year_form = Fourth_YearForm(request.POST)
        year_4 = Year_4.objects.filter(username=request.user).exists()
        if year_4 == True:
            return redirect("/already_exist/")

        if fourth_year_form.is_valid():
            form_fourth_year = fourth_year_form.save(commit=False)
            form_fourth_year.username = request.user
            form_fourth_year.save()
            messages.success(
                request, f'Your 4th Year has been Submitted Successfully!!!')
            return redirect("/technical_skills/")
    else:
        fourth_year_form = Fourth_YearForm()
    context = {
        "fourth_year_form": fourth_year_form,
    }
    return render(request, "final_resume/fourth_year.html", context)


@login_required(login_url='/login/')
def fourth_year_update(request):
    if request.method == "POST":
        form = Fourth_YearUpdateForm(
            request.POST, instance=request.user.year_4)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your Fourth Year form has been Updated Successfully!!!')
        return redirect("/")
    else:
        form = Fourth_YearUpdateForm(instance=request.user.year_4)
    return render(request, "update_and_delete/fourth_year_update.html", {"form": form})


@login_required(login_url='/login/')
def fourth_year_delete(request):
    ye_4 = Year_4.objects.filter(username=request.user).exists()
    if ye_4 == True:
        year_4 = Year_4.objects.get(username=request.user)
        year_4.delete()
        messages.success(
            request, f'Your Fourth Year form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")


# PERSONAL DETAIL CREATE, UPDATE AND DELETE
@login_required(login_url='/login/')
def technical_skills(request):
    if request.method == "POST":
        technical_skills_form = TechnicalSkillsForm(request.POST)
        technical_skills = Technical_Skills.objects.filter(
            username=request.user).exists()
        if technical_skills == True:
            return redirect("/already_exist/")

        if technical_skills_form.is_valid():
            tsf = technical_skills_form.save(commit=False)
            tsf.username = request.user
            tsf.save()
            messages.success(
                request, f'Your Technical Skills form has been Submitted Successfully!!!')
            return redirect("/Interests/")
    else:
        technical_skills_form = TechnicalSkillsForm()
    context = {
        "technical_skills_form": technical_skills_form,
    }
    return render(request, "final_resume/technical_skills.html", context)


@login_required(login_url='/login/')
def technical_skills_update(request):
    if request.method == "POST":
        form = TechnicalSkillsUpdateForm(
            request.POST, instance=request.user.technical_skills)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your Technical Skills form has been Updated Successfully!!!')
        return redirect("/")
    else:
        form = TechnicalSkillsUpdateForm(
            instance=request.user.technical_skills)

    context = {
        "form": form,
    }
    return render(request, "update_and_delete/technical_skills_update.html", context)


@login_required(login_url='/login/')
def technical_skills_delete(request):
    tech = Technical_Skills.objects.filter(username=request.user).exists()
    if tech == True:
        techs = Technical_Skills.objects.get(username=request.user)
        techs.delete()
        messages.success(
            request, f'Your Technical Skills form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")


# PERSONAL DETAIL CREATE, UPDATE AND DELETE
@login_required(login_url='/login/')
def interests(request):
    if request.method == "POST":
        interests_form = InterestsForm(request.POST)
        interests = Interests.objects.filter(
            username=request.user).exists()
        if interests == True:
            return redirect("/already_exist/")

        if interests_form.is_valid():
            in_f = interests_form.save(commit=False)
            in_f.username = request.user
            in_f.save()
            messages.success(
                request, f'Congratulations your forms has been Submitted Successfully!!!')
            messages.success(
                request, f'Check Your Resume Now!!!')
            return redirect("/")
    else:
        interests_form = InterestsForm()
    context = {
        "interests_form": interests_form,
    }
    return render(request, "final_resume/interests.html", context)


@login_required(login_url='/login/')
def interests_update(request):
    if request.method == "POST":
        form = InterestsUpdateForm(
            request.POST, instance=request.user.interests)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your Interests form has been Updated Successfully!!!')
        return redirect("/")
    else:
        form = InterestsUpdateForm(
            instance=request.user.interests)

    context = {
        "form": form,
    }
    return render(request, "update_and_delete/interests_update.html", context)


@login_required(login_url='/login/')
def interests_delete(request):
    inte = Interests.objects.filter(username=request.user).exists()
    if inte == True:
        intere = Interests.objects.get(username=request.user)
        intere.delete()
        messages.success(
            request, f'Your Interests form has been Deleted Successfully!!!')
        return redirect("/")
    else:
        return HttpResponse("No Record Found")

# For generating PDF invoice


@login_required(login_url='/login/')
def view_detail_pdf(request, *args, **kwargs):
    username = request.user
    # print("************************************")
    # print(username)
    prof = Profile.objects.filter(username=username).exists()
    # print(prof)
    if prof == True:
        profile = Profile.objects.get(username=username)
        # print(profile)
    else:
        profile = None

    pers = Personal_Detail.objects.filter(username=username).exists()
    if pers == True:
        personal_detail = Personal_Detail.objects.get(username=username)
    else:
        personal_detail = None

    add = Address.objects.filter(username=username).exists()
    if add == True:
        address = Address.objects.get(username=username)
    else:
        address = None

    st_10 = Std_10.objects.filter(username=username).exists()
    if st_10 == True:
        std_10 = Std_10.objects.get(username=username)
    else:
        std_10 = None

    st_12 = Std_12.objects.filter(username=username).exists()
    if st_12 == True:
        std_12 = Std_12.objects.get(username=username)
    else:
        std_12 = None

    ye_1 = Year_1.objects.filter(username=username).exists()
    if ye_1 == True:
        year_1 = Year_1.objects.get(username=username)
    else:
        year_1 = None

    ye_2 = Year_2.objects.filter(username=username).exists()
    if ye_2 == True:
        year_2 = Year_2.objects.get(username=username)
    else:
        year_2 = None

    ye_3 = Year_3.objects.filter(username=username).exists()
    if ye_3 == True:
        year_3 = Year_3.objects.get(username=username)
    else:
        year_3 = None

    ye_4 = Year_4.objects.filter(username=username).exists()
    if ye_4 == True:
        year_4 = Year_4.objects.get(username=username)
    else:
        year_4 = None

    tech = Technical_Skills.objects.filter(username=username).exists()
    if tech == True:
        technical_skills = Technical_Skills.objects.get(username=username)
    else:
        technical_skills = None

    inte = Interests.objects.filter(username=username).exists()
    if inte == True:
        interest = Interests.objects.get(username=username)
    else:
        interest = None

    cert = Certificate.objects.filter(username=username).exists()
    if cert == True:
        certificate = Certificate.objects.filter(username=request.user)
        coursera = Certificate.objects.filter(
            course_platform="COURSERA", username=username)
        udemy = Certificate.objects.filter(
            course_platform="UDEMY", username=username)
        edx = Certificate.objects.filter(
            course_platform="EDX", username=username)
        others = Certificate.objects.filter(
            course_platform="OTHERS", username=username)
        drawing = Certificate.objects.filter(
            course_platform="DRAWING", username=username)
        sports = Certificate.objects.filter(
            course_platform="SPORTS", username=username)
    else:
        certificate = None
        coursera = None
        udemy = None
        edx = None
        others = None
        drawing = None
        sports = None

    pro = Project.objects.filter(username=username).exists()
    if pro == True:
        projects = Project.objects.filter(username=username)
    else:
        projects = None

    context = {
        "profile": profile,
        "personal_detail": personal_detail,
        "address": address,
        "technical_skills": technical_skills,
        "interest": interest,
        "std_10": std_10,
        "std_12": std_12,
        "year_1": year_1,
        "year_2": year_2,
        "year_3": year_3,
        "year_4": year_4,
        "certificate": certificate,
        "coursera": coursera,
        "udemy": udemy,
        "edx": edx,
        "others": others,
        "drawing": drawing,
        "sports": sports,
        "projects": projects,
    }
    return render(request, "final_resume/pdf_detail.html", context)


@login_required(login_url='/login/')
def view_detail_pdf_images(request, *args, **kwargs):
    username = request.user
    # print("************************************")
    # print(username)
    prof = Profile.objects.filter(username=username).exists()
    # print(prof)
    if prof == True:
        profile = Profile.objects.get(username=username)
        # print(profile)
    else:
        profile = None

    pers = Personal_Detail.objects.filter(username=username).exists()
    if pers == True:
        personal_detail = Personal_Detail.objects.get(username=username)
    else:
        personal_detail = None

    add = Address.objects.filter(username=username).exists()
    if add == True:
        address = Address.objects.get(username=username)
    else:
        address = None

    st_10 = Std_10.objects.filter(username=username).exists()
    if st_10 == True:
        std_10 = Std_10.objects.get(username=username)
    else:
        std_10 = None

    st_12 = Std_12.objects.filter(username=username).exists()
    if st_12 == True:
        std_12 = Std_12.objects.get(username=username)
    else:
        std_12 = None

    ye_1 = Year_1.objects.filter(username=username).exists()
    if ye_1 == True:
        year_1 = Year_1.objects.get(username=username)
    else:
        year_1 = None

    ye_2 = Year_2.objects.filter(username=username).exists()
    if ye_2 == True:
        year_2 = Year_2.objects.get(username=username)
    else:
        year_2 = None

    ye_3 = Year_3.objects.filter(username=username).exists()
    if ye_3 == True:
        year_3 = Year_3.objects.get(username=username)
    else:
        year_3 = None

    ye_4 = Year_4.objects.filter(username=username).exists()
    if ye_4 == True:
        year_4 = Year_4.objects.get(username=username)
    else:
        year_4 = None

    tech = Technical_Skills.objects.filter(username=username).exists()
    if tech == True:
        technical_skills = Technical_Skills.objects.get(username=username)
    else:
        technical_skills = None

    inte = Interests.objects.filter(username=username).exists()
    if inte == True:
        interest = Interests.objects.get(username=username)
    else:
        interest = None

    cert = Certificate.objects.filter(username=username).exists()
    if cert == True:
        certificate = Certificate.objects.filter(username=request.user)
        coursera = Certificate.objects.filter(
            course_platform="COURSERA", username=username)
        udemy = Certificate.objects.filter(
            course_platform="UDEMY", username=username)
        edx = Certificate.objects.filter(
            course_platform="EDX", username=username)
        others = Certificate.objects.filter(
            course_platform="OTHERS", username=username)
        drawing = Certificate.objects.filter(
            course_platform="DRAWING", username=username)
        sports = Certificate.objects.filter(
            course_platform="SPORTS", username=username)
    else:
        certificate = None
        coursera = None
        udemy = None
        edx = None
        others = None
        drawing = None
        sports = None

    pro = Project.objects.filter(username=username).exists()
    if pro == True:
        projects = Project.objects.filter(username=username)
    else:
        projects = None

    context = {
        "profile": profile,
        "personal_detail": personal_detail,
        "address": address,
        "technical_skills": technical_skills,
        "interest": interest,
        "std_10": std_10,
        "std_12": std_12,
        "year_1": year_1,
        "year_2": year_2,
        "year_3": year_3,
        "year_4": year_4,
        "certificate": certificate,
        "coursera": coursera,
        "udemy": udemy,
        "edx": edx,
        "others": others,
        "drawing": drawing,
        "sports": sports,
        "projects": projects,
    }
    return render(request, "final_resume/pdf_detail_images.html", context)


@login_required(login_url='/login/')
def generate_pdf(request, *args, **kwargs):
    template = get_template("final_resume/tech_detail.html")

    username = request.user
    # print("************************************")
    # print(username)
    prof = Profile.objects.filter(username=username).exists()
    # print(prof)
    if prof == True:
        profile = Profile.objects.get(username=username)
        # print(profile)
    else:
        profile = None

    pers = Personal_Detail.objects.filter(username=username).exists()
    if pers == True:
        personal_detail = Personal_Detail.objects.get(username=username)
    else:
        personal_detail = None

    add = Address.objects.filter(username=username).exists()
    if add == True:
        address = Address.objects.get(username=username)
    else:
        address = None

    st_10 = Std_10.objects.filter(username=username).exists()
    if st_10 == True:
        std_10 = Std_10.objects.get(username=username)
    else:
        std_10 = None

    st_12 = Std_12.objects.filter(username=username).exists()
    if st_12 == True:
        std_12 = Std_12.objects.get(username=username)
    else:
        std_12 = None

    ye_1 = Year_1.objects.filter(username=username).exists()
    if ye_1 == True:
        year_1 = Year_1.objects.get(username=username)
    else:
        year_1 = None

    ye_2 = Year_2.objects.filter(username=username).exists()
    if ye_2 == True:
        year_2 = Year_2.objects.get(username=username)
    else:
        year_2 = None

    ye_3 = Year_3.objects.filter(username=username).exists()
    if ye_3 == True:
        year_3 = Year_3.objects.get(username=username)
    else:
        year_3 = None

    ye_4 = Year_4.objects.filter(username=username).exists()
    if ye_4 == True:
        year_4 = Year_4.objects.get(username=username)
    else:
        year_4 = None

    tech = Technical_Skills.objects.filter(username=username).exists()
    if tech == True:
        technical_skills = Technical_Skills.objects.get(username=username)
    else:
        technical_skills = None

    inte = Interests.objects.filter(username=username).exists()
    if inte == True:
        interest = Interests.objects.get(username=username)
    else:
        interest = None

    cert = Certificate.objects.filter(username=username).exists()
    if cert == True:
        certificate = Certificate.objects.filter(username=request.user)
        coursera = Certificate.objects.filter(
            course_platform="COURSERA", username=username)
        udemy = Certificate.objects.filter(
            course_platform="UDEMY", username=username)
        edx = Certificate.objects.filter(
            course_platform="EDX", username=username)
        others = Certificate.objects.filter(
            course_platform="OTHERS", username=username)
        drawing = Certificate.objects.filter(
            course_platform="DRAWING", username=username)
        sports = Certificate.objects.filter(
            course_platform="SPORTS", username=username)
        # print(certificate)

    else:
        certificate = None
        coursera = None
        udemy = None
        edx = None
        others = None
        drawing = None
        sports = None

    pro = Project.objects.filter(username=username).exists()
    if pro == True:
        projects = Project.objects.filter(username=username)
    else:
        projects = None

    context = {
        "profile": profile,
        "personal_detail": personal_detail,
        "address": address,
        "technical_skills": technical_skills,
        "interest": interest,
        "std_10": std_10,
        "std_12": std_12,
        "year_1": year_1,
        "year_2": year_2,
        "year_3": year_3,
        "year_4": year_4,
        "certificate": certificate,
        "coursera": coursera,
        "udemy": udemy,
        "edx": edx,
        "others": others,
        "drawing": drawing,
        "sports": sports,
        "projects": projects,
    }
    html = template.render(context)
    pdf = render_to_pdf("final_resume/tech_detail.html", context)
    if pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        filename = "%s_Resume.pdf" % (username)
        content = "inline; filename=%s" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" % (filename)
        response["Content-Disposition"] = content
        return response
    return HttpResponse("Not Found")


@login_required(login_url='/login/')
def generate_pdf_images(request, *args, **kwargs):
    template = get_template("final_resume/tech_detail_images.html")

    username = request.user
    # print("************************************")
    # print(username)
    prof = Profile.objects.filter(username=username).exists()
    # print(prof)
    if prof == True:
        profile = Profile.objects.get(username=username)
        # print(profile)
    else:
        profile = None

    pers = Personal_Detail.objects.filter(username=username).exists()
    if pers == True:
        personal_detail = Personal_Detail.objects.get(username=username)
    else:
        personal_detail = None

    add = Address.objects.filter(username=username).exists()
    if add == True:
        address = Address.objects.get(username=username)
    else:
        address = None

    st_10 = Std_10.objects.filter(username=username).exists()
    if st_10 == True:
        std_10 = Std_10.objects.get(username=username)
    else:
        std_10 = None

    st_12 = Std_12.objects.filter(username=username).exists()
    if st_12 == True:
        std_12 = Std_12.objects.get(username=username)
    else:
        std_12 = None

    ye_1 = Year_1.objects.filter(username=username).exists()
    if ye_1 == True:
        year_1 = Year_1.objects.get(username=username)
    else:
        year_1 = None

    ye_2 = Year_2.objects.filter(username=username).exists()
    if ye_2 == True:
        year_2 = Year_2.objects.get(username=username)
    else:
        year_2 = None

    ye_3 = Year_3.objects.filter(username=username).exists()
    if ye_3 == True:
        year_3 = Year_3.objects.get(username=username)
    else:
        year_3 = None

    ye_4 = Year_4.objects.filter(username=username).exists()
    if ye_4 == True:
        year_4 = Year_4.objects.get(username=username)
    else:
        year_4 = None

    tech = Technical_Skills.objects.filter(username=username).exists()
    if tech == True:
        technical_skills = Technical_Skills.objects.get(username=username)
    else:
        technical_skills = None

    inte = Interests.objects.filter(username=username).exists()
    if inte == True:
        interest = Interests.objects.get(username=username)
    else:
        interest = None

    cert = Certificate.objects.filter(username=username).exists()
    if cert == True:
        certificate = Certificate.objects.filter(username=request.user)
        coursera = Certificate.objects.filter(
            course_platform="COURSERA", username=username)
        udemy = Certificate.objects.filter(
            course_platform="UDEMY", username=username)
        edx = Certificate.objects.filter(
            course_platform="EDX", username=username)
        others = Certificate.objects.filter(
            course_platform="OTHERS", username=username)
        drawing = Certificate.objects.filter(
            course_platform="DRAWING", username=username)
        sports = Certificate.objects.filter(
            course_platform="SPORTS", username=username)

    else:
        certificate = None
        coursera = None
        udemy = None
        edx = None
        others = None
        drawing = None
        sports = None

    pro = Project.objects.filter(username=username).exists()
    if pro == True:
        projects = Project.objects.filter(username=username)
    else:
        projects = None

    context = {
        "profile": profile,
        "personal_detail": personal_detail,
        "address": address,
        "technical_skills": technical_skills,
        "interest": interest,
        "std_10": std_10,
        "std_12": std_12,
        "year_1": year_1,
        "year_2": year_2,
        "year_3": year_3,
        "year_4": year_4,
        "certificate": certificate,
        "coursera": coursera,
        "udemy": udemy,
        "edx": edx,
        "others": others,
        "drawing": drawing,
        "sports": sports,
        "projects": projects,
    }
    html = template.render(context)
    pdf = render_to_pdf("final_resume/tech_detail_images.html", context)
    if pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        filename = "%s_Resume_images.pdf" % (username)
        content = "inline; filename=%s" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" % (filename)
        response["Content-Disposition"] = content
        return response
    return HttpResponse("Not Found")
