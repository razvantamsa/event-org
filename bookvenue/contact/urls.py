from django.urls import path, include
from .views import CreateContactView

urlpatterns = [
    path('', CreateContactView.as_view()),
]