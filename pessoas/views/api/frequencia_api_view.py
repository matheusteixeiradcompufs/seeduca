from rest_framework import viewsets

from pessoas.models import Frequencia
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import FrequenciaSerializer


class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]