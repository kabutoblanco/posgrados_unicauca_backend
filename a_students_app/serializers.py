from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student, Program, Enrrollment, Agreement, Grant
from d_accounts_app.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups','user_permissions')
    


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



class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
  
    class Meta:
        model = Student
        fields = ('dedication', 'program','date_record','date_update','user')
    def create (self,validated_data):
        user_data = validated_data.pop ('user')             
                      
        user_instance = User.objects.create (**user_data)        
        
        student= Student.objects.create ( user= user_instance,**validated_data)
        return student