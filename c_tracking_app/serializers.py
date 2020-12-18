from rest_framework import serializers
from .models import Tracking, TestCoordinator, TestDirector, ActivityProfessor

from a_students_app.models import Student, Enrrollment
from b_activities_app.models import Activity
from d_accounts_app.models import User
from a_students_app.models import Program
from d_information_management_app.models import Professor


# Serializers
class TypeActiviyField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(TypeActiviyField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[0]

    def to_internal_value(self, data):
        return getattr(self._choices, data)


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


class ActivitySerializer(serializers.ModelSerializer):
    type = TypeActiviyField(choices=Activity.TYPE_CHOICES)
    student = StudentSerializer()

    class Meta:
        model = Activity
        fields = ("id", "title", "student", "description", "receipt", "state", "type", "start_date", "end_date", "academic_year")


class EnrrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Enrrollment
        fields = ('id', 'student', 'period', 'state')


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = '__all__'


class TestDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDirector
        fields = '__all__'

    def create(self, validate_data):
        validate_data['director'] = Professor.objects.get(user=validate_data['director'].id)
        test = TestDirector.objects.create(**validate_data)
        return test


class TestCoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCoordinator
        fields = '__all__'

    def create(self, validate_data):
        validate_data['coordinator'] = Professor.objects.get(user=validate_data['coordinator'].id)
        test = TestCoordinator.objects.create(**validate_data)
        return test