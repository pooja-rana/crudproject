from rest_framework.viewsets import ModelViewSet

from crudapp.models import User
from crudapp.permission import IsAdmin, IsNormalUserOrAdmin
from crudapp.serializers import UserDetailSerializer, RetrieveUserDetailsSerializer
from crudapp.authentication import TokenAuthentication

class UserViewSet(ModelViewSet):
    """This viewsets is used for the crud operation of user and admin"""

    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        """ Permission class based in user role"""
        if self.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        if self.action == 'retrieve':
            return [IsNormalUserOrAdmin()]
        return []

    def get_serializer_class(self):
        """
        This is get serializer method  for retrieve
        serializer based in request method
        """
        if self.action == 'create':
            return UserDetailSerializer
        return RetrieveUserDetailsSerializer
