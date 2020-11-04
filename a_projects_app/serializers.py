from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, General, Specific

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = "__all__"

class SpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specific
        fields = "__all__"
