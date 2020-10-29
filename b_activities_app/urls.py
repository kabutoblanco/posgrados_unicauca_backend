from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()

router.register('activity', ActivityViewSet)
router.register('lecture', LectureViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]