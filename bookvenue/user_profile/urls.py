from django.urls import path, include
from .views import UserDetail, edit_user

urlpatterns = [
    path('<str:slug>/', UserDetail.as_view()),
    path('', edit_user),
]
