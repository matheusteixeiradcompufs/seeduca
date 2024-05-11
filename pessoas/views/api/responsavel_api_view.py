from rest_framework import viewsets
from pessoas.models import Responsavel
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import ResponsavelSerializer


class ResponsavelViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet que fornece operações CRUD para Responsável.

    Esta ViewSet permite que os coordenadores acessem e gerenciem informações sobre os responsáveis.
    Os métodos CRUD (Create, Retrieve, Update, Delete) estão disponíveis nesta ViewSet.

    Os usuários devem ter permissões de Coordenador Full para acessar e modificar os dados dos responsáveis.

    """
    queryset = Responsavel.objects.all()  # Obtém todos os objetos de Responsavel do banco de dados
    serializer_class = ResponsavelSerializer  # Define a classe de serializador para Responsavel
    permission_classes = [
        CoordenadorFullPermission,  # Define as permissões necessárias para acessar esta ViewSet
    ]
