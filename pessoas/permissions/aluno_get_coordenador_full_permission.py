from rest_framework import permissions


class AlunoGetCoordenadorFullPermission(permissions.BasePermission):
    """
    Permissão personalizada para permitir que um usuário tenha acesso total se for um coordenador,
    diretor ou superusuário. Para outros métodos HTTP, a permissão é concedida apenas para métodos seguros.
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
        # Verifica se o usuário pertence aos grupos "Coordenador" ou "Diretor" ou é um superusuário.
        if request.user.groups.filter(name__in=['Coordenador', 'Diretor']).exists() or request.user.is_superuser:
            return True
        # Para outros métodos HTTP, apenas métodos seguros são permitidos.
        elif request.method in permissions.SAFE_METHODS:
            return True
        # Nega permissão para todos os outros casos.
        return False
