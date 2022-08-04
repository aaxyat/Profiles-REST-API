from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """ Test if user has permission"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id