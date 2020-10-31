from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()

router.register('tracking', TrackingAPI)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/student', StudentListAPI.as_view()),
    path('api/student/<int:id_student>/activity', ActivityListStudentAPI.as_view()),
    path('api/director/<int:id_professor>/activity', ActivityDirectorAPI.as_view()),
    path('api/coordinator/<int:id_professor>/activity', ActivityCoordinatorAPI.as_view())
]