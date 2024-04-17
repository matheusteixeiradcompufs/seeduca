from rest_framework import permissions


class DiretorEscolaPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Coordenador', 'Diretor', 'Professor']).exists() and request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False