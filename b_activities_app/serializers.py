from rest_framework import serializers

from .models import *

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'

class ProjectCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectCourse
        fields = '__all__'

class ResearchStaysSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchStays
        fields = '__all__'

class PresentationResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PresentationResults
        fields = '__all__'

class ParticipationProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParticipationProjects
        fields = '__all__'

class PrizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prize
        fields = '__all__'