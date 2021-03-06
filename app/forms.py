# app/forms.py
from django import forms

from .models import Post


class post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']
