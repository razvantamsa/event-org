from django.urls import path

from .views import PostListView, PostDetailView, create_post

urlpatterns = [
    path('', PostListView.as_view()),
    path('<slug>/', PostDetailView.as_view()),
    path('create-post', create_post),
]