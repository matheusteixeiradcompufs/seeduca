from rest_framework import viewsets
from pessoas.models import Boletim
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import BoletimSerializer


class BoletimViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para exibir e manipular informações dos boletins.

    Esta ViewSet permite a exibição, criação, atualização e exclusão de informações sobre os boletins.

    Requer permissões específicas para que os coordenadores tenham acesso completo aos boletins.
    """
    queryset = Boletim.objects.all()  # Define o conjunto de consultas para todos os boletins
    serializer_class = BoletimSerializer  # Define o serializador usado para a serialização e desserialização
    permission_classes = [
        CoordenadorFullPermission,  # Permissão necessária para que os coordenadores tenham acesso completo aos boletins
    ]
