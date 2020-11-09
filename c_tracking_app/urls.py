from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()

router.register('tracking', TrackingAPI)

router.register('test_director', TestDirectorAPI)
router.register('test_coordinator', TestCoordinatorAPI)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/student', StudentListAPI.as_view()),
    path('api/student/<int:id_student>', StudentAPI.as_view()),
    path('api/student/<int:id_student>/activity', ActivityListStudentAPI.as_view()),

    path('api/director/<int:id_professor>/activity', DirectorActiviesAPI.as_view()),
    path('api/director/<int:id_professor>/student', DirectorStudentsAPI.as_view()),
    path('api/coordinator/<int:id_professor>/activity', ActivityCoordinatorAPI.as_view()),

    path('api/director/<int:id_professor>/<int:id_activity>/test', TestDirectorListAPI.as_view()),
    path('api/coordinator/<int:id_professor>/<int:id_activity>/test', TestCoordinatorListAPI.as_view()),
]