from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Feed(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(max_length=300)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("posts_detail", kwargs={"pk": self.pk})


class Feed_Image(models.Model):
    id = models.AutoField(primary_key=True)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    feed_image = models.ImageField(
        upload_to="feed_image/", null=True, blank=True)
