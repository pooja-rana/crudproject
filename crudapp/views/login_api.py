from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from crudapp.models import AccessToken
from crudapp.serializers import LoginSerializer
from crudapp.serializers.access_token_serializer import AccessTokenSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            cell_number = serializer.validated_data['cell_number']
            password = serializer.validated_data['password']
            user = authenticate(request, username=cell_number, password=password)

            if user:
                token = AccessTokenSerializer.generate_token(user)
                return Response({"token": token.token, "expires_in": token.token_time_limit}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)