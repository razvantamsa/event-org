from django.urls import path, include

from authentication.views import * 

urlpatterns = [
    path('register/', register),
    path('login/', login_view),
    path('logout/', logout_view),
    path('change_pass/', change_pass_test),
    path('', display_welcome),
]