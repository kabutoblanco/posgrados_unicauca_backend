from rest_framework import serializers
from .models import (Country, State, City, Institution, Professor, Faculty, Department, InvestigationGroup, 
                    KnowledgeArea, InvestigationLine, WorksDepartm, ManageInvestLine, ManageInvestGroup, 
                    WorksInvestGroup, AcademicTraining, IsMember, WorksDepartm)

# Create your serializers here.
# --------------------------------------------------Arias

#País
class CountrySerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(required=False)
    class Meta:
        model = Country
        fields = "__all__"

    def create(self, validate_data):
        instance = Country.objects.create(**validate_data)
        instance.save()
        return instance

#Estado o Departamento
class StateSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(required=False)
    class Meta:
        model = State
        fields = "__all__"

    def create(self, validate_data):
        instance = State.objects.create(**validate_data)
        #instance.save()
        print("Serializer en state: ",instance)
        return instance

#Ciudad
class CitySerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(required=False)
    class Meta:
        model = City
        fields = "__all__"

    def create(self, validate_data):
        instance = City.objects.create(**validate_data)
        instance.save()
        return instance

#Institución
class InstitutionSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(required=False)
    class Meta:
        model = Institution
        fields = "__all__"

    def create(self, validate_data):
        instance = Institution.objects.create(**validate_data)
        instance.save()
        return instance

#Profesor
class ProfessorSerializer(serializers.ModelSerializer):
    is_director_student = serializers.BooleanField(required=False)
    is_director_gi = serializers.BooleanField(required=False)
    is_internal = serializers.BooleanField(required=False)
    status = serializers.BooleanField(required=False)
    class Meta:
        model = Professor
        fields = "__all__"

    def create(self, validate_data):
        instance = Professor.objects.create(**validate_data)
        instance.save()
        return instance

#Facultad
class FacultySerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(required=False)
    class Meta:
        model = Faculty
        fields = "__all__"

    def create(self, validate_data):
        instance = Faculty.objects.create(**validate_data)
        instance.save()
        return instance

#Departamento 
class DepartmentSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(required=False)
    class Meta:
        model = Department
        fields = "__all__"

    def create(self, validate_data):
        instance = Department.objects.create(**validate_data)
        instance.save()
        return instance
#Formación Academica
class AcademicTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicTraining
        fields = "__all__"

    def create(self, validate_data):
        instance = AcademicTraining.objects.create(**validate_data)
        instance.save()
        return instance

# Create your serializers here.
# --------------------------------------------------Jeison

#Grupo de investigacion
class InvestigationGroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    foundation_date = serializers.DateField(required=False)
    category = serializers.CharField(required=False)
    status = serializers.BooleanField(required=False)
    class Meta:
        model = InvestigationGroup
        fields = "__all__"
    
    def create(self, validate_data):
        instance = InvestigationGroup.objects.create(**validate_data)
        instance.save()
        return instance

#Area del conocimiento
class KnowledgeAreaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    status = serializers.BooleanField(required=False)
    class Meta:
        model = KnowledgeArea
        fields = "__all__"

    def create(self, validate_data):
        instance = KnowledgeArea.objects.create(**validate_data)
        instance.save()
        return instance

#Linea de investigacion
class InvestigationLineSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    status = serializers.BooleanField(required=False)
    class Meta:
        model = InvestigationLine
        fields = "__all__"

    def create(self, validate_data):
        instance = InvestigationLine.objects.create(**validate_data)
        instance.save()
        return instance

#Trabaja
class WorksInvestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksInvestGroup
        fields = '__all__'

    def create(self, validate_data):
        instance = WorksInvestGroup.objects.create(**validate_data)
        instance.save()
        return instance

#Maneja
class ManageInvestLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageInvestLine
        fields = '__all__'

    def create(self, validate_data):
        instance = ManageInvestLine.objects.create(**validate_data)
        instance.save()
        return instance

#Dirige
class ManageInvestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageInvestGroup
        fields = '__all__'

    def create(self, validate_data):
        instance = ManageInvestGroup.objects.create(**validate_data)
        instance.save()
        return instance

#Es miembro
class IsMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsMember
        fields = '__all__'

    def create(self, validate_data):
        instance = IsMember.objects.create(**validate_data)
        instance.save()
        return instance

class WorksDepartmSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksDepartm
        fields = '__all__'

    def create(self, validate_data):
        instance = WorksDepartm.objects.create(**validate_data)
        instance.save()
        return instance

class CoordinatorProgramSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=False)
    academic_period = serializers.CharField(required=False)
    class Meta:
        model = CoordinatorProgram
        fields = ['professor', 'program', 'academic_period', 'is_active']
    
    def create(self, validate_data):
        instance = CoordinatorProgram.objects.create(**validate_data)
        instance.save()
        return instance

