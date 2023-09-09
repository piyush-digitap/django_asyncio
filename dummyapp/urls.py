# dummyapp/urls.py

from django.urls import path
from .views import (ConcurrentApiCall, ConcurrentFunctionCall)

urlpatterns = [
    path('concurrent_api/', ConcurrentApiCall.as_view(),
         name='concurrent-api'),
    path('concurrent_function/',
         ConcurrentFunctionCall.as_view(),
         name='concurrent-function'),
]
