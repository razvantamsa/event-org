from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'address', 'picture1', 'picture2', 'picture3', 'picture4']