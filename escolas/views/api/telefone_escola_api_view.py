from rest_framework import viewsets

from escolas.models import TelefoneEscola
from escolas.serializers import TelefoneEscolaSerializer
from pessoas.permissions import DiretorEscolaPermission


class TelefoneEscolaViewSet(viewsets.ModelViewSet):
    queryset = TelefoneEscola.objects.all()
    serializer_class = TelefoneEscolaSerializer
    permission_classes = [
        DiretorEscolaPermission,
    ]