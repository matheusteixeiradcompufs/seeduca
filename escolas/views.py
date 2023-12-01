from rest_framework import viewsets, permissions

from escolas.models import Escola
from escolas.permissions import EscolaPermission
from escolas.serializers import EscolaSerializer


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
    permission_classes = [
        EscolaPermission,
    ]
