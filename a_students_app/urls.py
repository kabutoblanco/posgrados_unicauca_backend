from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, UserViewSet, EnrrollmentViewSet,ProgramViewSet, GrantViewSet, AgreementViewSet
from .api import CreateStudentProfessor,UpdateStudenAPI,UpdateGrantAPI,UpdateAgreementAPI, ReporteEstudiantesExcel, UpdateStudentProfessorAPI
router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('user', UserViewSet)
router.register('enrrollment', EnrrollmentViewSet)
router.register('program', ProgramViewSet)
router.register('grant', GrantViewSet)
router.register('agreement', AgreementViewSet)




urlpatterns = [
    path('',include(router.urls)),
    path('createstudentprofessor',CreateStudentProfessor.as_view()),
    path('updatestudent/<int:id>',UpdateStudenAPI.as_view()),
    path('updategrant/<int:id>',UpdateGrantAPI.as_view()),
    path('updateagreement/<int:id>',UpdateAgreementAPI.as_view()),
    path('report/<int:type>',ReporteEstudiantesExcel.as_view()),
    path('updatestudentprofessor/<int:id_s>/<int:id_p>',UpdateStudentProfessorAPI.as_view())
    ]