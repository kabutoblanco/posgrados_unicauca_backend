from rest_framework import serializers
from .models import Tracking, TestCoordinator, TestDirector

from a_students_app.models import Student, Enrrollment
from b_activities_app.models import Activity
from d_accounts_app.models import User
from a_students_app.models import Program


# Serializers
class TypeActiviyField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(TypeActiviyField, self).__init__(**kwargs)

    def to_representation(self, obj):
        # return obj
        return self._choices.get(obj)

    def to_internal_value(self, data):
        return getattr(self._choices, data)


class ActivitySerializer(serializers.ModelSerializer):
    type = TypeActiviyField(choices=Activity.TYPE_CHOICES)

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
        fields = ('id', 'first_name', 'last_name', 'photo')


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
