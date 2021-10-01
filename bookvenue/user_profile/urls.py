from django.urls import path, include
from .views import UserDetail

urlpatterns = [
    path('<str:slug>/', UserDetail.as_view())
]
