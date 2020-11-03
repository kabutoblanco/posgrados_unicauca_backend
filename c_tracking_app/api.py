from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from .models import *
from .serializers import *
from a_students_app.models import StudentProfessor
from .backends import IsDirector, IsCoordinador

from django.db.models import Avg, Sum, Count
from rest_framework.permissions import IsAuthenticated


# - - - - - PRIMER SPRINT - - - - -
class StudentAPI(views.APIView):
    """
    API usada para retornar un estudiante con fecha y estado del último cohorte de matricula
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    """

    # permission_classes = (IsAuthenticated, )
    serializer_class = EnrrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = Enrrollment.objects.filter(
            student__user=kwargs['id_student']).order_by('-period')[:1]
        try:
            return Response({"student": EnrrollmentSerializer(queryset[0]).data})
        except:
            return Response({"student": []})


class StudentListAPI(generics.RetrieveAPIView):
    """
    API usada para retornar la lista de estudiantes con fecha y estado del último cohorte de matricula
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    """

    # permission_classes = (IsAuthenticated, )
    serializer_class = EnrrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = Student.objects.filter(is_active=True)
        queryset_list = Enrrollment.objects.none()
        for student in queryset:
            queryset_list = queryset_list | Enrrollment.objects.filter(
                student__user=student.user.id).order_by('-period')[:1]
        return Response({"students": EnrrollmentSerializer(queryset_list, many=True).data})


class TrackingAPI(viewsets.ModelViewSet):
    """
    API usada para gestionar el modelo de Tracking
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = [IsAuthenticated, (IsDirector | IsCoordinador)]
    serializer_class = TrackingSerializer
    queryset = Tracking.objects.all()


class ActivityListStudentAPI(generics.RetrieveAPIView):
    """
    API usada para filtrar los registros del modelo Activity por estudiante
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = [IsAuthenticated, (IsDirector | IsCoordinador)]
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = Activity.objects.filter(
            is_active=True, student__user=kwargs['id_student'])
        return Response({"activities": ActivitySerializer(queryset, many=True).data})
# - - - - - PRIMER SPRINT - - - - -


# - - - - - SEGUNDO SPRINT - - - - -
class DirectorStudentsAPI(generics.RetrieveAPIView):
    """
    API usada para obtener los estudiantes que un director tiene a cargo
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = (IsAuthenticated, IsDirector)
    serializer_class = EnrrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = StudentProfessor.objects.filter(
            is_active=True, professor__user=kwargs['id_professor']).values('student')
        list = [e['student'] for e in queryset]
        queryset = Student.objects.filter(is_active=True, id__in=list)
        queryset_list = Enrrollment.objects.none()
        for student in queryset:
            queryset_list = queryset_list | Enrrollment.objects.filter(
                student__user=student.user.id).order_by('-period')[:1]
        return Response({"students": EnrrollmentSerializer(queryset_list, many=True).data})


class DirectorActiviesAPI(generics.RetrieveAPIView):
    """
    API usada para obtener las actividades que un director tiene de los estudiantes a cargo
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = (IsAuthenticated, IsDirector)
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = StudentProfessor.objects.filter(
            is_active=True, professor__user=kwargs['id_professor']).values('student')
        list = [e['student'] for e in queryset]
        queryset_list = Activity.objects.filter(is_active=True, student__in=list)
        return Response({"activities": ActivitySerializer(queryset_list, many=True).data})


class ActivityCoordinatorAPI(generics.RetrieveAPIView):
    """
    API usada para obtener las actividades que un coordinador tiene a cargo
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = (IsAuthenticated, IsCoordinador)
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = ActivityProfessor.objects.filter(
            is_active=True, professor__user=kwargs['id_professor'], rol=3).values('activity')
        list = [e['activity'] for e in queryset]
        queryset_list = Activity.objects.filter(is_active=True, id__in=list)
        return Response({"activities": ActivitySerializer(queryset_list, many=True).data})
# - - - - - SEGUNDO SPRINT - - - - -
