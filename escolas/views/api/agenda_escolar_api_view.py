from rest_framework import viewsets

from escolas.models import AgendaEscolar
from escolas.serializers import AgendaEscolarSerializer
from pessoas.permissions import CoordenadorFullPermission


class AgendaEscolarViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de agenda escolar de uma turma.

    Este endpoint permite listar, criar, atualizar e excluir agendas.
    """
    queryset = AgendaEscolar.objects.all()
    serializer_class = AgendaEscolarSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]