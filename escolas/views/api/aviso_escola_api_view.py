from rest_framework import viewsets

from escolas.models import AvisoEscola
from escolas.serializers import AvisoEscolaSerializer
from pessoas.permissions import CoordenadorFullPermission, GetPermission


class AvisoEscolaViewSet(viewsets.ModelViewSet):
    queryset = AvisoEscola.objects.all()
    serializer_class = AvisoEscolaSerializer
    permission_classes = [
        # CoordenadorFullPermission,
    ]