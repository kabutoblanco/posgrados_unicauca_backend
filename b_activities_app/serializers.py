from rest_framework import serializers

from .models import *

# Modulo B #

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

# Consultas a otros modulos #

from a_students_app.models import Program
from d_information_management_app.models import Institution, InvestigationLine, Professor, City, Country 

class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'

class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = '__all__'

class InvestigationLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvestigationLine
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'

# Consultas #

from a_students_app.models import Enrrollment

class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrrollment
        fields = [ 'period' ]
