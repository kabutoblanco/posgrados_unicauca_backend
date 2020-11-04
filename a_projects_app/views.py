from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, General, Specific
from .serializers import ProjectSerializer, GeneralSerializer, SpecificSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class GeneralViewSet(ModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer

class SpecificViewSet(ModelViewSet):
    queryset = Specific.objects.all()
    serializer_class = SpecificSerializer
