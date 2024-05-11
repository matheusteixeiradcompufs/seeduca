from rest_framework import viewsets
from pessoas.models import Transporte
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import TransporteSerializer


class TransporteViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet que fornece operações CRUD para transporte.

    Esta ViewSet permite que os coordenadores acessem e gerenciem informações sobre transporte.
    Os métodos CRUD (Create, Retrieve, Update, Delete) estão disponíveis nesta ViewSet.

    Os usuários devem ter permissões de Coordenador Full para acessar e modificar os dados de transporte.

    """
    queryset = Transporte.objects.all()  # Obtém todos os objetos de Transporte do banco de dados
    serializer_class = TransporteSerializer  # Define a classe de serializador para Transporte
    permission_classes = [
        CoordenadorFullPermission,  # Define as permissões necessárias para acessar esta ViewSet
    ]
