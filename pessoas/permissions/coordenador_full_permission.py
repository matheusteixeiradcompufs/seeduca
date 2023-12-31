from rest_framework import permissions


class CoordenadorFullPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Coordenadores', 'Diretores']).exists() or request.user.is_superuser:
            return True