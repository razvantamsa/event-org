from django import forms
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField

class ProfileForm (forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'city', 'country', 'phonenumber', 'birth_date', 'profile_picture')

        widgets = {
            'bio': forms.Textarea(attrs = {'class': 'form-control', 'required' : 'False'}),
            'city': forms.TextInput(attrs = {'class': 'form-control', 'required' : 'False'}),
            'country': forms.TextInput(attrs = {'class': 'form-control', 'required' : 'False'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs = {'class': 'form-control-file', 'required' : 'False'}),
        }
