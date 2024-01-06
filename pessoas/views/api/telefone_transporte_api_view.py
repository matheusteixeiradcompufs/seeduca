from rest_framework import viewsets

from pessoas.models import TelefoneTransporte
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import TelefoneTransporteSerializer


class TelefoneTransporteViewSet(viewsets.ModelViewSet):
    queryset = TelefoneTransporte.objects.all()
    serializer_class = TelefoneTransporteSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]