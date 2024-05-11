from rest_framework import viewsets

from escolas.models import Escola
from escolas.serializers import EscolaSerializer
from pessoas.permissions import DiretorEscolaPermission


class EscolaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de escolas.

    Este endpoint permite listar, criar, atualizar e excluir escolas.
    """
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
    permission_classes = [
        DiretorEscolaPermission,
    ]