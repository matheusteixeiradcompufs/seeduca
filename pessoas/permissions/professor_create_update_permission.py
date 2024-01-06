from rest_framework import permissions


class ProfessorCreateUpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Coordenadores', 'Diretores']).exists() or request.user.is_superuser:
            return True
        elif request.user.groups.filter(name='Professores').exists() and request.method in ['GET', 'POST', 'PATCH']:
            return True
        else:
            return False