from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from pessoas.models import Funcionario


class FuncionarioPermission(permissions.BasePermission):
    """
    Permissão personalizada para acessar recursos relacionados a funcionários.

    Esta permissão controla o acesso com base nos grupos de usuários e nos métodos de solicitação HTTP.
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
        usuario = request.user

        if usuario.is_superuser:
            # Superusuários têm acesso total.
            return True
        elif not usuario.groups.exists():
            # Usuários sem grupos não têm permissão.
            return False
        elif request.method == 'GET':
            # Métodos GET são permitidos.
            return True
        elif request.method == 'POST':
            # Verifica permissões ao criar um novo funcionário.
            if usuario.groups.filter(name='Professor').exists():
                # Professores não têm permissão para criar funcionários.
                return False
            elif usuario.groups.filter(name='Coordenador').exists():
                # Coordenadores podem criar funcionários com apenas um grupo 'Professor'.
                usuarioid = request.data.get('usuario', None)
                user = User.objects.get(pk=usuarioid)
                grupos = [objeto.id for objeto in list(user.groups.all())]
                return len(grupos) == 1 and 3 in grupos and 2 not in grupos and 1 not in grupos
            elif usuario.groups.filter(name='Diretor').exists():
                # Diretores podem criar funcionários com grupos 'Professor' ou 'Coordenador'.
                usuarioid = request.data.get('usuario', None)
                user = User.objects.get(pk=usuarioid)
                grupos = [objeto.id for objeto in list(user.groups.all())]
                return len(grupos) == 1 and (3 in grupos or 2 in grupos) and 1 not in grupos
            else:
                # Outros usuários não têm permissão para criar funcionários.
                return False
        return True

    def has_object_permission(self, request, view, obj):
        """
        Verifica se o usuário tem permissão para acessar ou modificar um objeto específico.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            view (APIView): A visualização que está sendo acessada.
            obj: O objeto sobre o qual a permissão é verificada.

        Returns:
            bool: Verdadeiro se o usuário tiver permissão, falso caso contrário.
        """
        usuario = request.user

        if usuario.is_superuser:
            # Superusuários têm acesso total.
            return True
        if request.method == 'GET' and obj is not None:
            # Permite acesso GET a funcionários.
            if usuario.groups.filter(name='Professor').exists():
                # Professores podem acessar apenas seus próprios dados.
                return usuario == obj.usuario or not obj.usuario.groups.exists()
            elif usuario.groups.filter(name='Coordenador').exists() and obj.usuario.groups.filter(name__in=['Professor', 'Coordenador']).exists():
                # Coordenadores podem acessar dados de professores e outros funcionários.
                return usuario == obj.usuario or not obj.usuario.groups.exists() or obj.usuario.groups.filter(name='Professor').exists()
            else:
                # Diretores podem acessar dados de todos os funcionários.
                return usuario.groups.filter(name='Diretor').exists() and obj.usuario.groups.filter(name__in=['Professor', 'Coordenador', 'Diretor']).exists() and (usuario == obj.usuario or not obj.usuario.groups.exists() or obj.usuario.groups.filter(name__in=['Professor', 'Coordenador']).exists())
        elif request.method == 'PATCH':
            # Permite a modificação de funcionários por coordenadores e diretores.
            usuarioid = obj.id
            user = User.objects.get(pk=usuarioid)
            grupos = [objeto.id for objeto in list(user.groups.all())]
            if usuario.groups.filter(name='Coordenador').exists() and obj.usuario.groups.filter(name='Professor').exists():
                # Coordenadores podem modificar apenas professores sem grupos adicionais.
                return len(grupos) == 0 or (len(grupos) == 1 and 3 in grupos and 2 not in grupos and 1 not in grupos)
            elif usuario.groups.filter(name='Diretor').exists() and (obj.usuario.groups.filter(name='Professor').exists() or obj.usuario.groups.filter(name='Coordenador').exists()):
                # Diretores podem modificar professores ou coordenadores sem grupos adicionais.
                return len(grupos) == 0 or (len(grupos) == 1 and (3 in grupos or 2 in grupos) and 1 not in grupos)
        else:
            # Permite a exclusão de funcionários por coordenadores e diretores.
            return request.method == 'DELETE' and (usuario.groups.filter(name='Coordenador').exists() and (obj.usuario.groups.filter(name='Professor').exists() or not obj.usuario.groups.exists())) or (usuario.groups.filter(name='Diretor').exists() and (obj.usuario.groups.filter(name='Professor').exists() or obj.usuario.groups.filter(name='Coordenador').exists() or not obj.usuario.groups.exists()))


class IsFuncionario(IsAuthenticated):
    """
    Verifica se o usuário autenticado é um funcionário.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário autenticado é um funcionário.

        Args:
            request (HttpRequest): O objeto de solicitação HTTP.
            view (APIView): A visualização que está sendo acessada.

        Returns:
            bool: Verdadeiro se o usuário autenticado for um funcionário, falso caso contrário.
        """
        user = request.user

        if user.is_superuser:
            # Superusuários têm acesso total.
            return True
        else:
            # Verifica se o usuário autenticado é um funcionário.
            funcionarios = Funcionario.objects.filter(usuario=user)
            return funcionarios.count() > 0
