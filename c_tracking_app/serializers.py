from rest_framework import serializers
from .models import Tracking, TestCoordinator, TestDirector

from a_students_app.models import Student
from b_activities_app.models import Activity
from d_accounts_app.models import User
from a_students_app.models import Program


# Serializers
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


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
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'user', 'program', 'activities')


class TrackingSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Tracking
        fields = ('id', 'state', 'student')


# Registers
class UpdateSeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = ("state", "enrrollment_date", "graduation_date",
                  "num_folio", "num_acta", "num_resolution", "observations")

    def update(self, instance, validated_data):
        instance.state = validated_data["state"]
        instance.enrrollment_date = validated_data["enrrollment_date"]
        instance.graduation_date = validated_data["graduation_date"]
        instance.num_folio = validated_data["num_folio"]
        instance.num_acta = validated_data["num_acta"]
        instance.num_resolution = validated_data["num_resolution"]
        instance.observations = validated_data["observations"]
        instance.save()
        return instance
