from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверяет, является ли текущий пользователь владельцем привычки."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
