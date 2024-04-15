from rest_framework import viewsets

from pessoas.models import Situacao
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers.situacao_serializer import SituacaoSerializer


class SituacaoViewSet(viewsets.ModelViewSet):
    queryset = Situacao.objects.all()
    serializer_class = SituacaoSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]