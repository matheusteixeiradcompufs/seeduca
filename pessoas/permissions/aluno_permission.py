from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from pessoas.models import Aluno


class AlunoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == 'GET' and not request.user.groups.exists():
            aluno_id = view.kwargs.get('pk')
            return str(request.user.usuario_pessoa.id) == str(aluno_id)
        elif request.method == 'GET' and request.user.groups.filter(name='Professores').exists():
            return True
        elif request.user.groups.filter(name__in=['Coordenadores', 'Diretores']).exists():
            return True


class IsAluno(IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        aluno = Aluno.objects.get(usuario=user)

        username = request.data.get('username')

        return aluno is not None and str(aluno) == username


class GetPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return request.method == 'GET'

