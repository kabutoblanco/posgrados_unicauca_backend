from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import *
from .serializers import *

from django.db.models import Avg, Sum, Count


# - - - - - PRIMER SPRINT - - - - -
class StudentListAPI(generics.RetrieveAPIView):
    serializer_class = EnrrollmentSerializer

    def get(self, request, *args, **kwargs):
        queryset = Student.objects.filter(is_active=True)
        queryset_list = Enrrollment.objects.none()
        for student in queryset:
            queryset_list = queryset_list | Enrrollment.objects.filter(student__user=student.user.id).order_by('-period')[:1]
        return Response({"students": EnrrollmentSerializer(queryset_list, many=True).data})


class TrackingAPI(viewsets.ModelViewSet):
    serializer_class = TrackingSerializer
    queryset = Tracking.objects.all()


class ActivityListStudentAPI(generics.RetrieveAPIView):
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = Activity.objects.filter(is_active=True, student=kwargs['id_student'])
        return Response({"activities": ActivitySerializer(queryset, many=True).data})
# - - - - - PRIMER SPRINT - - - - -


# - - - - - SEGUNDO SPRINT - - - - -
class ActivityProfessorAPI(generics.RetrieveAPIView):
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):        
        queryset = ActivityProfessor.objects.filter(is_active=True, professor=kwargs['id_professor']).values('activity__student')
        list = [e['activity__student'] for e in queryset]
        queryset = Student.objects.filter(is_active=True, id__in=list)
        queryset_list = Enrrollment.objects.none()
        for student in queryset:
            queryset_list = queryset_list | Enrrollment.objects.filter(student__user=student.user.id).order_by('-period')[:1]
        return Response({"students": EnrrollmentSerializer(queryset_list, many=True).data})
# - - - - - SEGUNDO SPRINT - - - - -