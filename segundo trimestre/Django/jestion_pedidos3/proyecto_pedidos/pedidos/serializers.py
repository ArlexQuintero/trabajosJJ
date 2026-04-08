from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data.get('username'),
            password=data.get('password')
        )
        if not user:
            raise serializers.ValidationError('Usuario o contraseña incorrectos.')
        if not user.is_active:
            raise serializers.ValidationError('Usuario inactivo.')
        data['user'] = user
        return data


class UserSerializer(serializers.Serializer):
    id       = serializers.IntegerField()
    username = serializers.CharField()
    email    = serializers.EmailField()
    is_staff = serializers.BooleanField()