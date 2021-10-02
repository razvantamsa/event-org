from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'required':'required', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required':'required', 'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count() == 0:
            raise ValidationError("User does not exist")
        if( not(username.isalnum() or username.isalpha()) ):
            raise ValidationError("User cannot contain invalid characters")
        return username

    def clean_repassword(self):
        password = self.cleaned_data['password']
        if( len(password)<8):
            raise forms.ValidationError("Password is too short")
        elif( len(password)>20):
            raise forms.ValidationError("Password is too long")
        return password

class SignUpForm(forms.ModelForm):
    captcha = CaptchaField()
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'required', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password']
        widgets = {
            'username': forms.TextInput({'required': 'required', 'class': 'form-control'}),
            'email': forms.EmailInput({'required': 'required', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'required': 'required', 'class': 'form-control'}),
            'first_name': forms.TextInput({'required': 'required', 'class': 'form-control'}),
            'last_name': forms.TextInput({'required': 'required', 'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email):
            raise forms.ValidationError("Email is not valid")
        elif User.objects.filter(email=email):
            raise forms.ValidationError("This email already exists")
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).count():
            raise forms.ValidationError("This username already exists")
        elif(not (username.isalnum() or username.isalpha()) ):
            raise forms.ValidationError("Username contains invalid characters")
        return username

    def clean_lastname(self):
        last_name = self.cleaned_data['last_name']
        if( not(last_name.isalpha())):
            raise forms.ValidationError("Last name contains invalid characters")
        return last_name
    
    def clean_firstname(self):
        first_name = self.cleaned_data['first_name']
        if( not(first_name.isalpha())):
            raise forms.ValidationError("First name contains invalid characters")
        return first_name

    def clean_repassword(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password.isdigit():
            raise forms.ValidationError("Password is entirely numerical")
        elif password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        elif( len(password1)<8):
            raise forms.ValidationError("Password is too short")
        elif( len(password1)>20):
            raise forms.ValidationError("Password is too long")
        return password2