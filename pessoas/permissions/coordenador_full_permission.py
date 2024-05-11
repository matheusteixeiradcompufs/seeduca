from rest_framework import permissions


class CoordenadorFullPermission(permissions.BasePermission):
    """
    Permissão personalizada para conceder acesso total aos usuários que pertencem aos grupos 'Coordenador' ou 'Diretor'
    ou são superusuários. Além disso, permite acesso seguro para usuários no grupo 'Professor'.
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
        # Verifica se o usuário pertence aos grupos 'Coordenador' ou 'Diretor' ou é um superusuário.
        if request.user.groups.filter(name__in=['Coordenador', 'Diretor']).exists() or request.user.is_superuser:
            return True
        # Verifica se o usuário pertence ao grupo 'Professor' e está tentando acessar um método seguro.
        elif request.user.groups.filter(name='Professor').exists() and request.method in permissions.SAFE_METHODS:
            return True
        # Nega permissão para todos os outros casos.
        return False
