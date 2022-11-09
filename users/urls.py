from django.contrib import admin
from django.urls import include, path

from .views import RegisterView, ShowProfileOfUser

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_user'),
    path('current/', ShowProfileOfUser.as_view(), name='show_user'),
]
