from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Allow read-only requests
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions only to owner
        return obj.author == request.user
