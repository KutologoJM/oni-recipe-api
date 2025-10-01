# accounts/permissions.py
from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):
    """
        Custom permission: Object-level write permissions are only
        allowed to admins. Read permissions are allowed to anyone.
        """

    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write access only for admin users
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Object-level write permissions are only
    allowed to the owner of the object. Read permissions are allowed to anyone.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the object has 'owner' attribute before comparing
        return hasattr(obj, "owner") and obj.owner == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission: Only the owner of the object or an admin
    user can view or edit it. Nobody else has access.
    """

    def has_object_permission(self, request, view, obj):
        # Check if user is the owner
        if hasattr(obj, "owner") and obj.owner == request.user:
            return True

        # Allow admins full access
        return request.user and request.user.is_staff


class IsNotAuthenticated(permissions.BasePermission):
    """
   Only allow access to unauthenticated users.
    """

    def has_permission(self, request, view):
        return not request.user or request.user.is_anonymous
