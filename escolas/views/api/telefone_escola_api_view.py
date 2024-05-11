from rest_framework import viewsets

from escolas.models import TelefoneEscola
from escolas.serializers import TelefoneEscolaSerializer
from pessoas.permissions import CoordenadorFullPermission


class TelefoneEscolaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de telefones de uma escola.

    Este endpoint permite listar, criar, atualizar e excluir telefones.
    """
    queryset = TelefoneEscola.objects.all()
    serializer_class = TelefoneEscolaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]