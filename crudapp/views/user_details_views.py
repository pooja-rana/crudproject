from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from crudapp.models import User
from crudapp.permission import IsAdmin, IsNormalUserOrAdmin
from crudapp.serializers import UserDetailSerializer, RetrieveUserDetailsSerializer


class UserViewSet(ModelViewSet):
    """This viewsets is used for the crud operation of user and admin"""
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        if self.action == 'retrieve':
            return [IsNormalUserOrAdmin()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserDetailSerializer
        return RetrieveUserDetailsSerializer
