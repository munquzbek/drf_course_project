from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """checks user is in moders group or not"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class IsOwner(BasePermission):
    """checks user is objects`s owner """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
