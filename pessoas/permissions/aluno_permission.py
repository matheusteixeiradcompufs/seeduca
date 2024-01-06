from rest_framework import permissions


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