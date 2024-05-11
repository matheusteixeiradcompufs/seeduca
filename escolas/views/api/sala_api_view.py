from rest_framework import viewsets

from escolas.models import Sala
from escolas.serializers import SalaSerializer
from pessoas.permissions import CoordenadorFullPermission


class SalaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de salas de uma escola.

    Este endpoint permite listar, criar, atualizar e excluir salas.
    """
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]