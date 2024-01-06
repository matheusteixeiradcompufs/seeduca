from rest_framework import viewsets

from pessoas.models import Transporte
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import TransporteSerializer


class TransporteViewSet(viewsets.ModelViewSet):
    queryset = Transporte.objects.all()
    serializer_class = TransporteSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]