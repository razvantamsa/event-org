from django.shortcuts import render

# Create your views here.

def register_test(request):
    return render(request, 'register.html')

def login_test(request):
    return render(request, 'login.html')

def logout_test(request):
    return render(request, 'logout.html')

def change_pass_test(request):
    return render(request, 'change_pass.html')
