from django.urls import path, include

from authentication.views import * 

urlpatterns = [
    path('register/', register_test),
    path('login/', login_test),
    path('logout/', logout_test),
    path('change_pass/', change_pass_test),
]