from rest_framework import viewsets

from escolas.models import DiaAgenda
from escolas.serializers import DiaAgendaSerializer
from pessoas.permissions import CoordenadorFullPermission


class DiaAgendaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de dias de uma agenda escolar.

    Este endpoint permite listar, criar, atualizar e excluir dias de uma agenda.
    """
    queryset = DiaAgenda.objects.all()
    serializer_class = DiaAgendaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]