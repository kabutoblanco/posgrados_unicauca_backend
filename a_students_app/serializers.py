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
        fields = ('id','dedication', 'program','date_record','date_update','user')
    def create (self,validated_data):
        print("sdsadasda")
        user_data = validated_data.pop ('user')
        user_instance = User.objects.create (**user_data)     
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
    
    class Meta:
        model = Student
        fields = ('dedication', 'program','user')
    