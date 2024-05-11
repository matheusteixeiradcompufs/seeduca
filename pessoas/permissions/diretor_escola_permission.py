from rest_framework import permissions


class DiretorEscolaPermission(permissions.BasePermission):
    """
    Permissão personalizada para permitir acesso a diretores de escola, coordenadores e professores
    para métodos seguros (GET, HEAD, OPTIONS) e para superusuários.
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
        # Verifica se o usuário pertence aos grupos 'Coordenador', 'Diretor' ou 'Professor' e está tentando
        # acessar um método seguro.
        if request.user.groups.filter(name__in=['Coordenador', 'Diretor', 'Professor']).exists() and \
                request.method in permissions.SAFE_METHODS:
            return True
        # Permite acesso para superusuários.
        elif request.user.is_superuser:
            return True
        # Nega permissão para todos os outros casos.
        return False
