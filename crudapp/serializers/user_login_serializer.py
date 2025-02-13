from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    cell_number = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user = authenticate(username=data['cell_number'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        return data