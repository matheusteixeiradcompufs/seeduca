from rest_framework import viewsets

from escolas.models import Escola
from escolas.serializers import EscolaSerializer
from pessoas.permissions import DiretorEscolaPermission


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
    permission_classes = [
        # DiretorEscolaPermission,
    ]