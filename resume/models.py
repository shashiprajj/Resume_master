from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
# Create your models here.


CATEGORY_CHOICES = (
    ('COURSERA', 'Coursera'),
    ('UDEMY', 'Udemy'),
    ('EDX', 'Edx'),
    ('DRAWING', 'Drawing'),
    ('SPORTS', 'Sports'),
    ('OTHERS', 'Others'),
)


class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_platform = models.CharField(choices=CATEGORY_CHOICES, max_length=8)
    course_img = models.ImageField(upload_to="certificates")
    date_completed = models.DateField(_("Date"), default=date.today)
    date_posted = models.DateTimeField(default=timezone.now)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})
