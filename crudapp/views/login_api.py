from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from crudapp.services import UserLoginService


class LoginView(APIView):
    """ This is login api view"""
    permission_classes = [AllowAny]

    def post(self, request):
        """ This is user login api"""
        response_data, response_status = UserLoginService().execute(request)
        return Response(response_data, status=response_status)