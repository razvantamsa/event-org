from django.urls import path

from .views import PostDetailView, create_post

urlpatterns = [
    path('create-post/', create_post ),
    path('post/<slug>/', PostDetailView.as_view()),
]