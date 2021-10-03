from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from post.models import Post
from django.contrib.auth.models import User
import logging
from django.core.mail import EmailMessage
import uuid
from user_profile.models import Profile
import json
from django.http import JsonResponse

# Create your views here.

# def search(request):
#     if request.method == "POST":
#         search_str = json.loads(request.body).get('searchText')
#         result_post = Post.objects.filter(title__starts_with=search_str) | Post.objects.filter(
#                     description__icontains=search_str) | Post.objects.filter(
#                     city__icontains=search_str) | Post.objects.filter(
#                     country__icontains=search_str) | Post.objects.filter(
#                     address__icontains=search_str)
#         data = result_post.value()
#         return JsonResponse( list(data), safe=False )


def display_welcome(request):
    post_list = Post.objects.all()
    user_list = User.objects.all()

    if(request.method == "GET"):
        str_search = request.GET.get('searchText')
        print(str_search)
        if (str_search):
            post_list = Post.objects.filter(title__icontains=str_search) | Post.objects.filter(
                                    host__username__icontains=str_search) | Post.objects.filter(
                                    address__icontains=str_search) | Post.objects.filter(
                                    city__icontains=str_search) | Post.objects.filter(
                                    country__icontains=str_search)
            user_list = User.objects.filter(username__icontains=str_search)

        order_post = request.GET.get('post_dropdown')
        order_user= request.GET.get('user_dropdown')
        if(order_post != None):
            post_list = post_list.order_by(order_post)

        if(order_user != None):
            user_list = user_list.order_by(order_user)

    context = {'post_list': post_list, 'user_list': user_list}
    string_name = 'anonymous'
    if request.user.is_authenticated:
        context['authenticated'] = True
        string_name = request.user.username
    else:
        context['authenticated'] = False
    context['name'] = string_name
    return render(request, "welcome.html", context)

def register(request):
    if request.user.is_authenticated:
        return render(request, "welcome_account.html")
    form = SignUpForm(data = request.POST or None)
    context = { 'form': form }
    context['name'] = 'anonymous'
    context['authenticated'] = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            #print(form.instance)
            user = authenticate(username = form.instance.username, password = form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
        else:
            logging.error("Form not valid")
    return render(request, 'register.html', context)

def login_view(request):
    errors = []
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(data = request.POST or None)
    context = {'form': form, 'errors': errors}
    context['name'] = 'anonymous'
    context['authenticated'] = False
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            errors.append("There is no such user/password")
    return render(request, 'login.html', context)

def logout_view(request):
    if(request.user.is_authenticated):
        logout(request)
    return redirect('/')

def change_pass(request):
    recipient = 'razvantamsa420@gmail.com'
    if(request.user.is_authenticated == True):
        recipient = request.user.email
    code = uuid.uuid4().hex[:6].upper()
    msg = EmailMessage('Forgot Password', 'Here is the code:' + code, to=[recipient])
    msg.send()
    return render(request, 'change_pass.html')
