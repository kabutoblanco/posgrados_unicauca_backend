from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, UserViewSet, EnrrollmentViewSet, StudentApiView

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('user', UserViewSet)
router.register('enrrollment', EnrrollmentViewSet)




urlpatterns = [
    path('',include(router.urls)),
    path('api/student/all',StudentApiView.as_view())
]