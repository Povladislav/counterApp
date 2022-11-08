from django.contrib import admin
from django.urls import include, path

from .views import RegisterView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_user'),
    path('all/', UserView.as_view(), name='show_users'),
]
