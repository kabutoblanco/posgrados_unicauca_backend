from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .backends import *

from .models import *
from .serializers import *

# Modulo B #
class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, (IsStudent | IsDirector | IsCoordinador)]
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LectureViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, (IsStudent | IsDirector | IsCoordinador)]
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, (IsStudent | IsDirector | IsCoordinador)]
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class ProjectCourseViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, (IsStudent | IsDirector | IsCoordinador)]
    queryset = ProjectCourse.objects.all()
    serializer_class = ProjectCourseSerializer

class ResearchStaysViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, (IsStudent | IsDirector | IsCoordinador)]
    queryset = ResearchStays.objects.all()
    serializer_class = ResearchStaysSerializer

class PresentationResultsViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, (IsStudent | IsDirector | IsCoordinador)]
    queryset = PresentationResults.objects.all()
    serializer_class = PresentationResultsSerializer

class ParticipationProjectsViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, (IsStudent | IsDirector | IsCoordinador)]
    queryset = ParticipationProjects.objects.all()
    serializer_class = ParticipationProjectsSerializer

class PrizeViewSet(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer

# Consultas a otros modulos #
from a_students_app.models import Program
from d_information_management_app.models import Institution, InvestigationLine, Professor, City, Country 

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class InvestigationLineViewSet(viewsets.ModelViewSet):
    queryset = InvestigationLine.objects.all()
    serializer_class = InvestigationLineSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

# Otras Consultas #
from a_students_app.models import Enrrollment
from rest_framework.response import Response

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED
)
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Avg, Sum, Count

class PeriodAPI(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        queryset = Enrrollment.objects.filter(student__user=kwargs['id_user']).values('period').order_by('-period')[:1]

        return HttpResponse(content=json.dumps(queryset[0], cls=DjangoJSONEncoder), status=HTTP_200_OK, content_type="application/json")
        
class PeriodsAPI(generics.RetrieveAPIView):
    serializer_class = PeriodSerializer

    def get(self, request, *args, **kwargs):
        queryset = Enrrollment.objects.filter(student__user=kwargs['id_user']).values('period').annotate(total=Count('period') )
        return Response({"list_period": PeriodSerializer(queryset, many=True).data})

class ActivitiesAPI(generics.RetrieveAPIView):
    serializer_class = ActivitySerializer

    def get(self, request, *args, **kwargs):
        queryset = Activity.objects.filter(student__user=kwargs['id_user'], academic_year=kwargs['academic_year'])
        return Response({"list_activities": ActivitySerializer(queryset, many=True).data})    