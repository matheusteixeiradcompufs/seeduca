from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from pessoas.models import Funcionario


class FuncionarioPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        usuario = request.user
        if usuario.is_superuser:
            return True

        elif not usuario.groups.exists():
            return False

        elif request.method == 'GET' and view.kwargs.get('pk') is None:
            if usuario.groups.filter(name='Professor').exists():
                return False

        elif request.method == 'POST':
            if usuario.groups.filter(name='Professor').exists():
                return False

            elif usuario.groups.filter(name='Coordenador').exists():
                grupos = request.data.get('groups', [])
                return len(grupos) == 1 and '3' in grupos and '2' not in grupos and '1' not in grupos

            elif usuario.groups.filter(name='Diretor').exists():
                grupos = request.data.get('groups', [])
                return len(grupos) == 1 and ('3' in grupos or '2' in grupos) and '1' not in grupos
            else:
                return False

        return True

    def has_object_permission(self, request, view, obj):

        usuario = request.user
        if usuario.is_superuser:
            return True

        if request.method == 'GET' and obj is not None:
            if usuario.groups.filter(name='Professor').exists():
                return usuario == obj.usuario or not obj.usuario.groups.exists()

            elif usuario.groups.filter(name='Coordenador').exists() and obj.usuario.groups.filter(name__in=['Professor', 'Coordenador']).exists():
                return usuario == obj.usuario or not obj.usuario.groups.exists() or obj.usuario.groups.filter(name='Professor').exists()

            else:
                return usuario.groups.filter(name='Diretor').exists() and obj.usuario.groups.filter(name__in=['Professor', 'Coordenador', 'Diretor']).exists() and (usuario == obj.usuario or not obj.usuario.groups.exists() or obj.usuario.groups.filter(name__in=['Professor', 'Coordenador']).exists())
                # return usuario == obj.usuario or not obj.usuario.groups.exists() or obj.usuario.groups.filter(name__in=['Professor', 'Coordenador']).exists()

        elif request.method == 'PATCH':
            grupos = request.data.get('groups', [])
            if usuario.groups.filter(name='Coordenador').exists() and obj.usuario.groups.filter(name='Professor').exists():
                return len(grupos) == 0 or (len(grupos) == 1 and '3' in grupos and '2' not in grupos and '1' not in grupos)

            elif usuario.groups.filter(name='Diretor').exists() and (obj.usuario.groups.filter(name='Professor').exists() or obj.usuario.groups.filter(name='Coordenador').exists()):
                return len(grupos) == 0 or (len(grupos) == 1 and ('3' in grupos or '2' in grupos) and '1' not in grupos)

        else:
            return request.method == 'DELETE' and (usuario.groups.filter(name='Coordenador').exists() and (obj.usuario.groups.filter(name='Professor').exists() or not obj.usuario.groups.exists())) or (usuario.groups.filter(name='Diretor').exists() and (obj.usuario.groups.filter(name='Professor').exists() or obj.usuario.groups.filter(name='Coordenador').exists() or not obj.usuario.groups.exists()))


class IsFuncionario(IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        if user.is_superuser:
            return True
        else:
            funcionario = Funcionario.objects.get(usuario=user)

            username = request.data.get('username')

            return funcionario is not None and str(funcionario) == username