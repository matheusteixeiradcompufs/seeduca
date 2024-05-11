from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from pessoas.models import Aluno


class AlunoPermission(permissions.BasePermission):
    """
    Permissão personalizada para acessar recursos relacionados a alunos.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário tem permissão para acessar a visualização.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            view (APIView): A visualização que está sendo acessada.

        Returns:
            bool: Verdadeiro se o usuário tiver permissão, falso caso contrário.
        """
        if request.user.is_superuser:
            return True
        elif request.method == 'GET' and not request.user.groups.exists():
            # Para usuários não pertencentes a nenhum grupo, permite apenas acesso ao próprio registro de aluno.
            aluno_id = view.kwargs.get('pk')
            return str(request.user.usuario_pessoa.id) == str(aluno_id)
        elif request.method == 'GET' and request.user.groups.filter(name='Professor').exists():
            # Professores têm permissão de leitura.
            return True
        elif request.user.groups.filter(name__in=['Coordenador', 'Diretor']).exists():
            # Coordenadores e diretores têm acesso total.
            return True
        # Caso nenhuma condição seja atendida, nega a permissão.
        return False


class IsAluno(IsAuthenticated):
    """
    Verifica se o usuário autenticado é um aluno.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário autenticado é um aluno.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            view (APIView): A visualização que está sendo acessada.

        Returns:
            bool: Verdadeiro se o usuário autenticado for um aluno, falso caso contrário.
        """
        user = request.user

        if user.is_superuser:
            # Superusuários não são alunos.
            return False
        else:
            # Verifica se o usuário é um aluno.
            alunos = Aluno.objects.filter(usuario=user)
            return alunos.count() > 0
