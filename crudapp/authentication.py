from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import AccessToken
from crudapp.messages import CrudOperationMessages

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return None

        try:
            access_token = AccessToken.objects.get(token=token)
            return (access_token.user, None)
        except AccessToken.DoesNotExist:
            raise AuthenticationFailed(CrudOperationMessages.INVALID_TOKEN)
