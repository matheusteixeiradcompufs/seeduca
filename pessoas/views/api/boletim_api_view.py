from rest_framework import viewsets

from pessoas.models import Boletim
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import BoletimSerializer


class BoletimViewSet(viewsets.ModelViewSet):
    queryset = Boletim.objects.all()
    serializer_class = BoletimSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]