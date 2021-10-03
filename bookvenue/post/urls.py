from django.urls import path

from .views import PostDetailView, create_post, delete_post, PostUpdateView

urlpatterns = [
    path('create-post/', create_post ),
    path('post/<slug>/', PostDetailView.as_view()),
    path('post/<slug>/edit/', PostUpdateView.as_view()),
    path('post/<slug>/delete/', delete_post),
]