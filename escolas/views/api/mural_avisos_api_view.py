from rest_framework import viewsets

from escolas.models import MuralAvisos
from escolas.serializers import MuralAvisosSerializer
from pessoas.permissions import CoordenadorFullPermission


class MuralAvisosViewSet(viewsets.ModelViewSet):
    queryset = MuralAvisos.objects.all()
    serializer_class = MuralAvisosSerializer
    permission_classes = [
        CoordenadorFullPermission
    ]