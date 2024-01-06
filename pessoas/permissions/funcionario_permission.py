from rest_framework import permissions


class FuncionarioPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        usuario = request.user
        if usuario.is_superuser:
            return True

        elif not usuario.groups.exists():
            return False

        elif request.method == 'GET' and view.kwargs.get('pk') is None:
            if usuario.groups.filter(name='Professores').exists():
                return False

        elif request.method == 'POST':
            if usuario.groups.filter(name='Professores').exists():
                return False

            elif usuario.groups.filter(name='Coordenadores').exists():
                grupos = request.data.get('grupos_add', [])
                return len(grupos) == 1 and 'Professores' in grupos and 'Coordenadores' not in grupos and 'Diretores' not in grupos

            elif usuario.groups.filter(name='Diretores').exists():
                grupos = request.data.get('grupos_add', [])
                return len(grupos) == 1 and ('Professores' in grupos or 'Coordenadores' in grupos) and 'Diretores' not in grupos
            else:
                return False

        return True

    def has_object_permission(self, request, view, obj):

        usuario = request.user
        if usuario.is_superuser:
            return True

        if request.method == 'GET' and obj is not None:
            if usuario.groups.filter(name='Professores').exists():
                return usuario == obj.usuario or not obj.usuario.groups.exists()

            elif usuario.groups.filter(name='Coordenadores').exists() and obj.usuario.groups.filter(name__in=['Professores', 'Coordenadores']).exists():
                return usuario == obj.usuario or not obj.usuario.groups.exists() or obj.usuario.groups.filter(name='Professores').exists()

            else:
                return usuario.groups.filter(name='Diretores').exists() and obj.usuario.groups.filter(name__in=['Professores', 'Coordenadores', 'Diretores']).exists() and (usuario == obj.usuario or not obj.usuario.groups.exists() or obj.usuario.groups.filter(name__in=['Professores', 'Coordenadores']).exists())
                # return usuario == obj.usuario or not obj.usuario.groups.exists() or obj.usuario.groups.filter(name__in=['Professores', 'Coordenadores']).exists()

        elif request.method == 'PATCH':
            grupos = request.data.get('grupos_add', [])
            if usuario.groups.filter(name='Coordenadores').exists() and obj.usuario.groups.filter(name='Professores').exists():
                return len(grupos) == 0 or (len(grupos) == 1 and 'Professores' in grupos and 'Coordenadores' not in grupos and 'Diretores' not in grupos)

            elif usuario.groups.filter(name='Diretores').exists() and (obj.usuario.groups.filter(name='Professores').exists() or obj.usuario.groups.filter(name='Coordenadores').exists()):
                return len(grupos) == 0 or (len(grupos) == 1 and ('Professores' in grupos or 'Coordenadores' in grupos) and 'Diretores' not in grupos)

        else:
            return request.method == 'DELETE' and (usuario.groups.filter(name='Coordenadores').exists() and (obj.usuario.groups.filter(name='Professores').exists() or not obj.usuario.groups.exists())) or (usuario.groups.filter(name='Diretores').exists() and (obj.usuario.groups.filter(name='Professores').exists() or obj.usuario.groups.filter(name='Coordenadores').exists() or not obj.usuario.groups.exists()))