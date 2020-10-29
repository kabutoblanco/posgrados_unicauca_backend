from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import TrackingListAPI

router = DefaultRouter()

# router.register('traking', SeguimientoListAPI, basename='seui')

urlpatterns = [
    path('api/tracking', TrackingListAPI.as_view())
]