from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'address', 'picture1', 'picture2', 'picture3', 'picture4']

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'description': forms.Textarea(attrs = {'class': 'form-control'}),
            'address': forms.TextInput(attrs = {'class': 'form-control'}),
            'picture1': forms.FileInput(attrs = {'class': 'form-control-file'}),
            'picture2': forms.FileInput(attrs = {'class': 'form-control-file'}),
            'picture3': forms.FileInput(attrs = {'class': 'form-control-file'}),
            'picture4': forms.FileInput(attrs = {'class': 'form-control-file'}),
        }