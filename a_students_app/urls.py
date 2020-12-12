from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, UserViewSet, EnrrollmentViewSet,ProgramViewSet, GrantViewSet, AgreementViewSet
from .api import CreateStudentProfessor
router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('user', UserViewSet)
router.register('enrrollment', EnrrollmentViewSet)
router.register('program', ProgramViewSet)
router.register('grant', GrantViewSet)
router.register('agreement', AgreementViewSet)




urlpatterns = [
    path('',include(router.urls)),
    path('createstudentprofessor',CreateStudentProfessor.as_view())
    ]