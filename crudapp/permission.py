from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', None) == 1

class IsNormalUserOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.role == 2