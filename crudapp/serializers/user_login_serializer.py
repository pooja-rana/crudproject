from django.contrib.auth import authenticate
from rest_framework import serializers
from crudapp.messages import CrudOperationMessages


class LoginSerializer(serializers.Serializer):
    """ login details validate serializer"""
    cell_number = serializers.CharField(
        required=True,
        error_messages={
            "required":CrudOperationMessages.ENTITY_REQUIRED_FIELD
        })
    password = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            "required": CrudOperationMessages.ENTITY_REQUIRED_FIELD
        }
                                     )

    def validate(self, data):
        user = authenticate(username=data['cell_number'], password=data['password'])
        if not user:
            raise serializers.ValidationError(CrudOperationMessages.INVALID_CREDENTIALS)
        return data