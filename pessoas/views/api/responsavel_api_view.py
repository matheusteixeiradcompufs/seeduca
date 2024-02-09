from rest_framework import viewsets

from pessoas.models import Responsavel
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import ResponsavelSerializer


class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    permission_classes = [
        # CoordenadorFullPermission,
    ]