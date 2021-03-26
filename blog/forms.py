from .models import Blog
from django.forms import ModelForm

class PostCreation(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','blog_content']