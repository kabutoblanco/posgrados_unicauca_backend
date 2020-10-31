from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import *
from .serializers import *

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class ProjectCourseViewSet(viewsets.ModelViewSet):
    queryset = ProjectCourse.objects.all()
    serializer_class = ProjectCourseSerializer

class ResearchStaysViewSet(viewsets.ModelViewSet):
    queryset = ResearchStays.objects.all()
    serializer_class = ResearchStaysSerializer

class PresentationResultsViewSet(viewsets.ModelViewSet):
    queryset = PresentationResults.objects.all()
    serializer_class = PresentationResultsSerializer

class ParticipationProjectsViewSet(viewsets.ModelViewSet):
    queryset = ParticipationProjects.objects.all()
    serializer_class = ParticipationProjectsSerializer

class PrizeViewSet(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer

# --- #

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