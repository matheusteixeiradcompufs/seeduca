from rest_framework import viewsets
from pessoas.models import Avaliacao
from pessoas.permissions import ProfessorUpdatePermission
from pessoas.serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para exibir e manipular informações de avaliações.

    Esta ViewSet permite a exibição, criação, atualização e exclusão de informações sobre as avaliações.

    Requer permissões específicas para que os professores possam atualizar as avaliações.
    """
    queryset = Avaliacao.objects.all()  # Define o conjunto de consultas para todas as avaliações
    serializer_class = AvaliacaoSerializer  # Define o serializador usado para a serialização e desserialização
    permission_classes = [
        ProfessorUpdatePermission,  # Permissão necessária para os professores atualizarem as avaliações
    ]
