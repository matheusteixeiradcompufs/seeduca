from rest_framework import viewsets
from pessoas.models import TelefonePessoa
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import TelefonePessoaSerializer


class TelefonePessoaViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet que fornece operações CRUD para números de telefone associados a pessoas.

    Esta ViewSet permite que coordenadores acessem e gerenciem informações sobre números de telefone associados a pessoas.
    Os métodos CRUD (Create, Retrieve, Update, Delete) estão disponíveis nesta ViewSet.

    Os usuários devem ter permissões de coordenador completo para acessar esta ViewSet.

    """
    queryset = TelefonePessoa.objects.all()  # Obtém todos os objetos de TelefonePessoa do banco de dados
    serializer_class = TelefonePessoaSerializer  # Define a classe de serializador para TelefonePessoa
    permission_classes = [
        CoordenadorFullPermission,  # Define a permissão necessária para acessar esta ViewSet
    ]
