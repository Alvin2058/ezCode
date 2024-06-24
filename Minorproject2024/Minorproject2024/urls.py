# Minorproject2024/Minorproject2024/urls.py

from django.contrib import admin
from django.urls import path, include
from Minorproject2024 import views  # Import views from your 'minor' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),  # Maps root URL to home views
]


