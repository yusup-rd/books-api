from rest_framework import permissions
from rest_framework.exceptions import APIException


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom permission class allowing full access to authors and read-only access to others."""

    def has_permission(self, request, view):
        """Check whether the request should be granted permission."""
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.groups.filter(name='Author').exists() or request.user.is_superuser:
            return True

        exception = APIException(
            detail="You do not have permission to perform this action. Only authors are allowed."
        )
        exception.status_code = 403
        raise exception
