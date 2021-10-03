from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'address','city', 'country', 'picture1', 'picture2', 'picture3', 'picture4']

        widgets = {
            'title': forms.TextInput({'required':'required', 'class': 'form-control'}),
            'description': forms.Textarea({'required':'required', 'class': 'form-control'}),
            'city': forms.TextInput({'required':'required', 'class': 'form-control'}),
            'country': forms.TextInput({'required':'required', 'class': 'form-control'}),
            'address': forms.TextInput({'required':'required', 'class': 'form-control'}),
            'picture1': forms.FileInput({'required':'required'}),
            'picture2': forms.FileInput({'required':'required'}),
            'picture3': forms.FileInput({'required':'required'}),
            'picture4': forms.FileInput({'required':'required'}),
        }