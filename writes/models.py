from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Poem(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    poem_title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    poem_description = models.TextField(max_length=1000, default=None)

    def __str__(self):
        return self.poem_title

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class Poem_Images(models.Model):
    id = models.AutoField(primary_key=True)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    poem_image = models.ImageField(
        upload_to="poem_image/", blank=True, null=True)

    def __str__(self):
        return self.poem.poem_title
