from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from crudapp.constant import CommonConst
from crudapp.models import User
from crudapp.messages import CrudOperationMessages

class UserDetailSerializer(serializers.ModelSerializer):
    """Detailed user serializer with validation for creating users."""
    name = serializers.CharField(
        required=True,
        max_length=255,
        error_messages={
            "required": CrudOperationMessages.ENTITY_REQUIRED_FIELD,
            "max_length": CrudOperationMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=255)
        }
    )
    email = serializers.EmailField(
        required=True,
        max_length=64,
        validators=[
            UniqueValidator(queryset=User.objects.all(),
                            message=CrudOperationMessages.EMAIL_ALREADY_EXISTS),
        ],
        error_messages={
            "invalid": CrudOperationMessages.INVALID_EMAIL,
            "required": CrudOperationMessages.ENTITY_REQUIRED_FIELD,
            "blank": CrudOperationMessages.ENTITY_REQUIRED_FIELD,
            "max_length": CrudOperationMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=64)
        }

    )
    cell_number = serializers.RegexField(
        required=True,
        regex=CommonConst.CELL_NUMBER.value,
        allow_null=True,
        allow_blank=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(),
                            message=CrudOperationMessages.CELL_NUM_ALREADY_EXISTS),
        ],
        error_messages={
            "invalid": CrudOperationMessages.ENTITY_WITH_CELL_NUMBER,
        }
    )
    password = serializers.RegexField(
        write_only=True,
        required=True,
        max_length=64,
        regex=CommonConst.PASSWORD_REGEX.value,
        error_messages={
            "invalid": CrudOperationMessages.INVALID_PASSWORD,
            "required": CrudOperationMessages.ENTITY_REQUIRED_FIELD,
            "blank": CrudOperationMessages.ENTITY_REQUIRED_FIELD,
            "max_length": CrudOperationMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=64),
        })

    role = serializers.ChoiceField(
        required=True,
        choices=User.ROLE_CHOICES,
        error_messages={
            "required": CrudOperationMessages.ENTITY_REQUIRED_FIELD,
        }
    )

    class Meta:
        model = User
        fields = (
            'id', 'profile_pic', 'name', 'cell_number', 'email', 'password','role',
        )

    def save(self, **kwargs):
        user = super(UserDetailSerializer, self).save(**kwargs)
        user_password = self.validated_data.get('password', '')
        if user_password:
            user.set_password(user_password)
            user.save()
        return user



class RetrieveUserDetailsSerializer(serializers.ModelSerializer):
    """This serializer is used for the retrieve user details"""

    class Meta:
        model = User
        fields = ('id', 'profile_pic', 'name', 'cell_number', 'email', 'role', 'created', 'modified')


