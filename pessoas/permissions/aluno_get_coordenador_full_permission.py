from rest_framework import permissions


class AlunoGetCoordenadorFullPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Coordenador', 'Diretor']).exists() or request.user.is_superuser:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True