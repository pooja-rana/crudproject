from rest_framework import status

from crudapp.messages import CrudOperationMessages
from crudapp.models import User
from crudapp.serializers import LoginSerializer
from crudapp.serializers.access_token_serializer import AccessTokenSerializer


class UserLoginService:

    def execute(self, request):
        """ main logic of user login"""
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            cell_number = serializer.validated_data['cell_number']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(cell_number=cell_number)
            except User.DoesNotExist:
                return {"error": CrudOperationMessages.INVALID_CREDENTIALS}

            if user.check_password(password):
                token = AccessTokenSerializer.generate_token(user)
                return {"token": token.token, 'user_id': user.id}, status.HTTP_200_OK
            else:
                return {"error": CrudOperationMessages.INVALID_CREDENTIALS}, status.HTTP_400_BAD_REQUEST

        return serializer.errors, status.HTTP_400_BAD_REQUEST