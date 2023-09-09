# dummyproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('dummyapp.urls')),  # Include your app's URLs here
]
