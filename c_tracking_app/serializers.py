from rest_framework import serializers
from .models import Tracking, TestCoordinator, TestDirector

from a_students_app.models import Student, Enrrollment
from b_activities_app.models import Activity
from d_accounts_app.models import User
from a_students_app.models import Program


# Serializers
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ("id", "title", "description", "receipt", "state", "type", "start_date", "end_date", "academic_year")


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ("id", "name",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    program = ProgramSerializer()
    # activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'user', 'program')


class EnrrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Enrrollment
        fields = ('id', 'student', 'period', 'state')


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = '__all__'
