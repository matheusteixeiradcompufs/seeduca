from rest_framework import viewsets

from escolas.models import Sala
from escolas.serializers import SalaSerializer
from pessoas.permissions import CoordenadorFullPermission


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]