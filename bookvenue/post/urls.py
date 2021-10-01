from django.urls import path

from .views import PostDetailView, create_post

urlpatterns = [
    path('<slug>/', PostDetailView.as_view()),
    path('create-post', create_post),
]