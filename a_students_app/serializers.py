from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student, Program, Enrrollment, Agreement, Grant, StudentProfessor
from d_accounts_app.models import User
from d_information_management_app.models import Professor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups','user_permissions')
    
class StudentProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfessor
        fields = "__all__"
    
    def create (self,validated_data):
        instance= StudentProfessor.objects.create(**validated_data)
        instance.save()
        return instance
        
     
    

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

class EnrrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrrollment
        fields = "__all__"

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = "__all__"
    

class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields = "__all__"

'''class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__" '''


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ('id','dedication', 'program','academic_title','instituion_degree','city_intituion','country_intituion','city_origin','departament_origin','date_record','date_update','user')
    def create (self,validated_data):
        
        user_data = validated_data.pop ('user')
        user_instance = User.objects.create (**user_data) 
        user_instance.set_password(user_data.get("password"))    
        student= Student.objects.create ( user= user_instance,**validated_data)
             
        return student

    '''def update(self, instance, validated_data):
        print("...actualiza",instance,validated_data)
        user_data = validated_data.pop ('user')
        user_instance = User.objects.update (**user_data)
        student= Student.objects.update ( user= user_instance,**validated_data)
        #instance.name = validated_data.get('name', instance.name)
        #instance.save()
        return student'''


class UpdateStudentSerializer(serializers.ModelSerializer):
    dedication = serializers.IntegerField(required=False)
    academic_title = serializers.CharField(required=False)
    
    class Meta:
        model = Student
        fields = ('dedication', 'program','user','academic_title')

class UpdateGrant(serializers.ModelSerializer):
    long = serializers.IntegerField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    name = serializers.CharField(required=False)
    announcement = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    num_resolution = serializers.CharField(required=False)
    class Meta:
        model = Grant
        fields = ('long','start_date','end_date','name', 'announcement','description','num_resolution')

class UpdateAgreement(serializers.ModelSerializer):
    long = serializers.IntegerField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    agreement_date = serializers.DateField(required=False)
    period_academic = serializers.CharField(required=False)
    percentage_discount = serializers.FloatField(required=False)
    observation = serializers.CharField(required=False)
    class Meta:
        model = Agreement
        fields = ('long','start_date','end_date','agreement_date', 'period_academic','percentage_discount','observation')
    
class UpdateStudentProfessor(serializers.ModelSerializer):
    rol = serializers.IntegerField(required=False)
        
    class Meta:
        model = StudentProfessor
        fields = ('student', 'professor','rol')
    
    