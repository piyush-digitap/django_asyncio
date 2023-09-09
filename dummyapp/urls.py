# dummyapp/urls.py

from django.urls import path
from .views import ConcurrentApiView
from .function import ConcurrentApiView as CAV

urlpatterns = [
    path('concurrent_api/', ConcurrentApiView.as_view(),
         name='concurrent-api'),
    path('concurrent_function/', CAV.as_view(), name='concurrent-function'),
]
