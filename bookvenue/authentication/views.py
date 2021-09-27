from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
import logging

# Create your views here.

def display_welcome(request):
    if request.user.is_authenticated:
        return render(request, "welcome_account.html")
    return render(request, "welcome_anonymous.html")

def register(request):
    if request.user.is_authenticated:
        return render(request, "welcome_account.html")
    form = SignUpForm(data = request.POST or None)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            user = authenticate(username = form.instance.username, password = form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
        else:
            logging.error("Form not valid")
    return render(request, 'register.html', { 'form': form })

def login_view(request):
    errors = []
    if request.user.is_authenticated:
        return render(request, "welcome_account.html")
    form = LoginForm(data = request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, user)
            if request.user.is_authenticated == True:
                return redirect('/')
            errors.append("There is no such user/password")
    return render(request, 'login.html', {'form': form, 'errors': errors})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def change_pass_test(request):
    return render(request, 'change_pass.html')
