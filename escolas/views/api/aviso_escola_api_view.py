from rest_framework import viewsets

from escolas.models import AvisoEscola
from escolas.serializers import AvisoEscolaSerializer
from pessoas.permissions import CoordenadorFullPermission


class AvisoEscolaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de avisos de um mural.

    Este endpoint permite listar, criar, atualizar e excluir avisos.
    """
    queryset = AvisoEscola.objects.all()
    serializer_class = AvisoEscolaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]