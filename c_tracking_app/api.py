from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from .models import *
from .serializers import *
from a_students_app.models import StudentProfessor
from .backends import IsDirector, IsCoordinador
from django.db.models import Avg, Sum, Count, Q
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
                student__user=student.user).order_by('-period')[:1]
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


class ActivityAPI(generics.RetrieveAPIView):
    """
    API usada para obtener una actividad por id
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    """

    # permission_classes = [IsAuthenticated, (IsDirector | IsCoordinador)]
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = Activity.objects.get(id=kwargs['id'])
        return Response({"activity": ActivitySerializer(queryset[0]).data})


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
        queryset = ActivityProfessor.objects.filter(Q(rol=1) | Q(rol=2))
        queryset = queryset.filter(
            is_active=True, professor__user=kwargs['id_professor'], ).values('activity')
        list = [e['activity'] for e in queryset]
        queryset_list = Activity.objects.filter(
            is_active=True, id__in=list)
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

    def intersection(self, lst1, lst2):
        print(lst2)
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        return lst3

    def get(self, request, *args, **kwargs):
        queryset = ActivityProfessor.objects.filter(
            is_active=True, professor__user=kwargs['id_professor'], rol=3).values('activity')
        list = [e['activity'] for e in queryset]
        queryset_1 = TestDirector.objects.filter(
            is_active=True, activity__in=list).values('activity')[:1]
        print(list)
        list_1 = [e['activity'] for e in queryset_1]
        list = self.intersection(list, list_1)
        queryset_list = Activity.objects.filter(is_active=True, id__in=list)
        return Response({"activities": ActivitySerializer(queryset_list, many=True).data})
# - - - - - SEGUNDO SPRINT - - - - -


# - - - - - TERCER SPRINT - - - - -
class TestDirectorAPI(viewsets.ModelViewSet):
    """
    API usada para gestionar el modelo de TestDirector
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    """

    # permission_classes = [IsAuthenticated, IsDirector]
    serializer_class = TestDirectorSerializer
    queryset = TestDirector.objects.all()


class TestCoordinatorAPI(viewsets.ModelViewSet):
    """
    API usada para gestionar el modelo de TestCoordinator
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsCoordinator
        El usuario debe tener a cargo al menos una actividad como coordinator
    """

    # permission_classes = [IsAuthenticated, IsCoordinador]
    serializer_class = TestCoordinatorSerializer
    queryset = TestCoordinator.objects.all()


class TestDirectorListAPI(generics.RetrieveAPIView):
    """
    API usada para obtener todas las evaluaciones de una actividad
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    """

    # permission_classes = [IsAuthenticated, IsDirector]
    serializer_class = TestDirectorSerializer

    def get(self, request, *args, **kwargs):
        queryset = TestDirector.objects.filter(
            is_active=True, activity=kwargs['id_activity'], director__user=kwargs['id_professor'])
        return Response({"test_activities": TestDirectorSerializer(queryset, many=True).data})


class TestCoordinatorListAPI(generics.RetrieveAPIView):
    """
    API usada para obtener todas las evaluaciones de una actividad
    - - - - -
    Permissions
    - - - - -
    IsAuthenticated
        El usuario debe tener un token que lo valide
    IsDirector
        El usuario debe tener a cargo al menos un estudiante como director o coodirector
    """

    # permission_classes = [IsAuthenticated, IsCoordinador]
    serializer_class = TestCoordinatorSerializer

    def get(self, request, *args, **kwargs):
        queryset = TestCoordinator.objects.filter(
            is_active=True, activity=kwargs['id_activity'], coordinator__user=kwargs['id_professor'])
        return Response({"test_activities": TestCoordinatorSerializer(queryset, many=True).data})
# - - - - - TERCER SPRINT - - - - -
