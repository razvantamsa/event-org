from django.urls import path, include
from .views import UserDetail, ProfileUpdateView

urlpatterns = [
    path('<str:slug>/', UserDetail.as_view()),
    path('', ProfileUpdateView.as_view()),
]
