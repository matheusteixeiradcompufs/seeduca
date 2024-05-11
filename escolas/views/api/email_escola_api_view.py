from rest_framework import viewsets

from escolas.models import EmailEscola
from escolas.serializers import EmailEscolaSerializer
from pessoas.permissions import CoordenadorFullPermission


class EmailEscolaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de emails de uma escola.

    Este endpoint permite listar, criar, atualizar e excluir emails.
    """
    queryset = EmailEscola.objects.all()
    serializer_class = EmailEscolaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]