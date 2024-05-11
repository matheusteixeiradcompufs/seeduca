from rest_framework import viewsets
from pessoas.models import TelefoneTransporte
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import TelefoneTransporteSerializer


class TelefoneTransporteViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet que fornece operações CRUD para telefones de transporte.

    Esta ViewSet permite que os coordenadores acessem e gerenciem informações sobre os telefones de transporte.
    Os métodos CRUD (Create, Retrieve, Update, Delete) estão disponíveis nesta ViewSet.

    Os usuários devem ter permissões de Coordenador Full para acessar e modificar os dados dos telefones de transporte.

    """
    queryset = TelefoneTransporte.objects.all()  # Obtém todos os objetos de TelefoneTransporte do banco de dados
    serializer_class = TelefoneTransporteSerializer  # Define a classe de serializador para TelefoneTransporte
    permission_classes = [
        CoordenadorFullPermission,  # Define as permissões necessárias para acessar esta ViewSet
    ]
