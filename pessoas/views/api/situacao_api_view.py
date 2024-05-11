from rest_framework import viewsets
from pessoas.models import Situacao
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers.situacao_serializer import SituacaoSerializer


class SituacaoViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet que fornece operações CRUD para Situação.

    Esta ViewSet permite que os coordenadores acessem e gerenciem informações sobre as situações dos alunos.
    Os métodos CRUD (Create, Retrieve, Update, Delete) estão disponíveis nesta ViewSet.

    Os usuários devem ter permissões de Coordenador Full para acessar e modificar os dados das situações.

    """
    queryset = Situacao.objects.all()  # Obtém todos os objetos de Situacao do banco de dados
    serializer_class = SituacaoSerializer  # Define a classe de serializador para Situacao
    permission_classes = [
        CoordenadorFullPermission,  # Define as permissões necessárias para acessar esta ViewSet
    ]
