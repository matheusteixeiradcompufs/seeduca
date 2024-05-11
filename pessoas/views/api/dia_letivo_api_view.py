from rest_framework import viewsets
from pessoas.models import DiaLetivo
from pessoas.permissions import ProfessorCreateUpdatePermission
from pessoas.serializers import DiaLetivoSerializer


class DiaLetivoViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para exibir e manipular informações dos dias letivos.

    Esta ViewSet permite a exibição, criação, atualização e exclusão de informações sobre os dias letivos.

    Requer permissões específicas para que os professores possam criar e atualizar os dias letivos.
    """
    queryset = DiaLetivo.objects.all()  # Define o conjunto de consultas para todos os dias letivos
    serializer_class = DiaLetivoSerializer  # Define o serializador usado para a serialização e desserialização
    permission_classes = [
        ProfessorCreateUpdatePermission,  # Permissão necessária para que os professores possam criar e atualizar os dias letivos
    ]
