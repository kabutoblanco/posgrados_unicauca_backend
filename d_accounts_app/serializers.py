from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


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
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'type_id', 'personal_id', 
                'personal_code', 'photo', 'telephone', 'address', 'is_proffessor', 'is_student', ]

    def create(self, validate_data):
        instance = User.objects.create(**validate_data)
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance