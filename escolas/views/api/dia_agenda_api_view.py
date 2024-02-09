from rest_framework import viewsets

from escolas.models import DiaAgenda
from escolas.serializers import DiaAgendaSerializer
from pessoas.permissions import CoordenadorFullPermission


class DiaAgendaViewSet(viewsets.ModelViewSet):
    queryset = DiaAgenda.objects.all()
    serializer_class = DiaAgendaSerializer
    permission_classes = [
        # CoordenadorFullPermission,
    ]