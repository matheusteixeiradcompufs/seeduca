from rest_framework import viewsets
from pessoas.models import Frequencia
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import FrequenciaSerializer


class FrequenciaViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para exibir e manipular informações de frequências.

    Esta ViewSet permite a exibição, criação, atualização e exclusão de informações sobre as frequências dos alunos.

    Requer permissões específicas para que os coordenadores tenham acesso completo às informações de frequência.
    """
    queryset = Frequencia.objects.all()  # Define o conjunto de consultas para todas as frequências
    serializer_class = FrequenciaSerializer  # Define o serializador usado para a serialização e desserialização
    permission_classes = [
        CoordenadorFullPermission,  # Permissão necessária para que os coordenadores tenham acesso completo às informações de frequência
    ]
