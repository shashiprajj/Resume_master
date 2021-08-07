from django.contrib import admin
from .models import Poem, Poem_Images
# Register your models here.


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "poem_title"]


@admin.register(Poem_Images)
class PoemImagesAdmin(admin.ModelAdmin):
    list_display = ["poem", "poem_image"]
