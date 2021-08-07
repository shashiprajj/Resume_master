from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from .views import CourseDetailView, StudentRegistrationView
from . import views as myauth_views
from django.contrib.auth import views as auth_views
from .forms import StudentPasswordChangeForm, StudentPasswordResetForm, StudentSetPasswordForm

urlpatterns = [

    path("register/", views.StudentRegistrationView.as_view(), name="register"),
    path("login/", myauth_views.StudentLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("passwordchange/", auth_views.PasswordChangeView.as_view(template_name="login_system/passwordchange.html",
                                                                  form_class=StudentPasswordChangeForm,
                                                                  success_url="/passwordchangedone/"), name="passwordchange"),
    path("passwordchangedone/", auth_views.PasswordChangeDoneView.as_view(template_name="login_system/passwordchangedone.html"),
         name="passwordchangedone"),

    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="login_system/password_reset.html",
                                                                 form_class=StudentPasswordResetForm), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="login_system/password_reset_done.html"),
         name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="login_system/password_reset_confirm.html",
                                                                                                 form_class=StudentSetPasswordForm), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="login_system/password_reset_complete.html"),
         name="password_reset_complete"),


    path("", views.home, name="home"),
    path("home_update", views.home_update, name="home_update"),
    #     path("all_certificates/", views.all_certificates, name="all_certificates"),
    #     path("coursera/", views.coursera, name="coursera"),
    #     path("udemy/", views.udemy, name="udemy"),
    #     path("edx/", views.edx, name="edx"),
    #     path("others/", views.others, name="others"),
    #     path("all_certificates/<int:pk>",
    #          views.CourseDetailView.as_view(), name="course_detail"),
    #     path("all_poems/", views.all_poems, name="all_poems"),
    #     path("friends/", views.friends, name="friends"),
    #     path("projects/", views.projects, name="projects"),
    #     path("resume/", views.resume, name="resume"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
