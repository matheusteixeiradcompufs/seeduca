from rest_framework import viewsets
from pessoas.models import AgendaRecados
from pessoas.permissions import AlunoGetCoordenadorFullPermission
from pessoas.serializers import AgendaRecadosSerializer


class AgendaRecadosViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para exibir e manipular a agenda de recados.

    Esta ViewSet permite a exibição, criação, atualização e exclusão de recados na agenda.

    Requer permissões para alunos obterem acesso completo e coordenadores.
    """
    queryset = AgendaRecados.objects.all()  # Define o conjunto de consultas para todos os objetos AgendaRecados
    serializer_class = AgendaRecadosSerializer  # Define o serializador usado para a serialização e desserialização
    permission_classes = [
        AlunoGetCoordenadorFullPermission,  # Permissão necessária para alunos obterem acesso completo e coordenadores
    ]
