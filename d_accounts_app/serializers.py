from rest_framework import serializers
from knox.models import AuthToken
from django.contrib.auth import authenticate
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'personal_id', 'username', 'email')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")

class CreateUserSerializer(serializers.ModelSerializer):
    is_coordinator = serializers.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'type_id', 'personal_id', 
                'personal_code', 'photo', 'telephone', 'address', 'is_coordinator']

    def create(self, validate_data):
        instance = User.objects.create(**validate_data)
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

class ConsultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'type_id', 'personal_id', 
                'personal_code', 'photo', 'telephone', 'address', 'is_student', 'is_proffessor', 'is_coordinator']

class UpdateUserSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    type_id = serializers.IntegerField(required=False)
    personal_id = serializers.CharField(required=False)
    personal_code = serializers.CharField(required=False)
    photo = serializers.FileField(required=False)
    telephone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    is_proffessor = serializers.BooleanField(required=False)
    is_student = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)
    is_coordinator = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'type_id', 'personal_id', 
                'personal_code', 'photo', 'telephone', 'address', 'is_proffessor', 'is_student', 'is_active', 
                'is_coordinator']
    
    def update(self, instance, validate_data):
        for attr, value in validate_data.items(): 
            if attr == 'password': 
                instance.set_password(value) 
            else: 
                setattr(instance, attr, value) 
        instance.save() 
        return instance 


