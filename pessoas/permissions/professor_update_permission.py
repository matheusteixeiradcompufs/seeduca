from rest_framework import permissions


class ProfessorUpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Coordenador', 'Diretor']).exists() or request.user.is_superuser:
            return True
        elif request.user.groups.filter(name='Professor').exists() and request.method in ['GET', 'PATCH']:
            return True
        else:
            return False