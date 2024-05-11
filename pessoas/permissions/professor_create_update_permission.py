from rest_framework import permissions


class ProfessorCreateUpdatePermission(permissions.BasePermission):
    """
    Permissão personalizada para criar e atualizar informações.

    Esta permissão permite que coordenadores, diretores e superusuários criem, recuperem, atualizem e deletem informações.
    Professores também podem criar e atualizar informações.
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
        if request.user.groups.filter(name__in=['Coordenador', 'Diretor']).exists() or request.user.is_superuser:
            # Coordenadores, diretores e superusuários têm acesso total.
            return True
        elif request.user.groups.filter(name='Professor').exists() and request.method in ['GET', 'POST', 'PATCH']:
            # Professores podem criar, atualizar e recuperar informações.
            return True
        else:
            # Para todos os outros casos, nega-se a permissão.
            return False
