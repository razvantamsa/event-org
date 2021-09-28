from django.urls import path, include

from authentication.views import * 

urlpatterns = [
    path('register/', register),
    path('login/', login_view),
    path('logout/', logout_view),
    path('forgot-password/', change_pass),
    path('', display_welcome),
]