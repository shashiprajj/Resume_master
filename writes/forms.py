from django import forms
from .models import Poem, Poem_Images


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ["poem_title", "date_posted", "poem_description"]


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ["poem_title", "date_posted", "poem_description"]
