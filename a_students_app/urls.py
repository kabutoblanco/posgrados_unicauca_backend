from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, UserViewSet, EnrrollmentViewSet,ProgramViewSet, StudentProfessortViewSet, GrantViewSet, AgreementViewSet

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('user', UserViewSet)
router.register('enrrollment', EnrrollmentViewSet)
router.register('program', ProgramViewSet)
router.register('studentprofessor', StudentProfessortViewSet)
router.register('grant', GrantViewSet)
router.register('agreement', AgreementViewSet)




urlpatterns = [
    path('',include(router.urls))
    ]