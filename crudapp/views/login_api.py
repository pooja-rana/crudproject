from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from crudapp.models import User
from crudapp.serializers import LoginSerializer
from crudapp.serializers.access_token_serializer import AccessTokenSerializer
from crudapp.messages import CrudOperationMessages


class LoginView(APIView):
    """ This is login api view"""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            cell_number = serializer.validated_data['cell_number']
            password = serializer.validated_data['password']

            # Check if the user exists with cell_number
            try:
                user = User.objects.get(cell_number=cell_number)
            except User.DoesNotExist:
                return Response({"error": CrudOperationMessages.INVALID_CREDENTIALS},
                                status=status.HTTP_400_BAD_REQUEST)

            if user.check_password(password):
                token = AccessTokenSerializer.generate_token(user)
                return Response({"token": token.token, 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                return Response({"error": CrudOperationMessages.INVALID_CREDENTIALS}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)