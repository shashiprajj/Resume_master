from django.contrib import admin
from .models import Feed, Feed_Image
# Register your models here.


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "date_posted"]


@admin.register(Feed_Image)
class FeedImageAdmin(admin.ModelAdmin):
    list_display = ["id", "feed", "feed_image"]
