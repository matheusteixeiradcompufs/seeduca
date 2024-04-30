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
        elif request.method == 'GET' and request.user.groups.filter(name='Professor').exists():
            return True
        elif request.user.groups.filter(name__in=['Coordenador', 'Diretor']).exists():
            return True


class IsAluno(IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        if user.is_superuser:
            return False
        else:
            alunos = Aluno.objects.filter(usuario=user)

            return alunos.count() > 0


