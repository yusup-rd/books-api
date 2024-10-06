from rest_framework import permissions
from rest_framework.exceptions import APIException


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.groups.filter(name='Author').exists():
            return True

        exception = APIException(
            detail="You do not have permission to perform this action. Only authors are allowed to perform this action."
        )
        exception.status_code = 403
        raise exception
