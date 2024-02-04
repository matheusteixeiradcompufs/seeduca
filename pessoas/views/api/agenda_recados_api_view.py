from rest_framework import viewsets

from pessoas.models import AgendaRecados
from pessoas.permissions import AlunoPermission
from pessoas.serializers import AgendaRecadosSerializer


class AgendaRecadosViewSet(viewsets.ModelViewSet):
    queryset = AgendaRecados.objects.all()
    serializer_class = AgendaRecadosSerializer
    permission_classes = [
        # AlunoPermission,
    ]