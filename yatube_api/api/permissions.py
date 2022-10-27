from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """"Не дает пользователю удалять/редактировать объекты других авторов"""

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
