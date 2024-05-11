from rest_framework import viewsets

from escolas.models import MuralAvisos
from escolas.serializers import MuralAvisosSerializer
from pessoas.permissions import CoordenadorFullPermission


class MuralAvisosViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de murais de avisos de uma escola.

    Este endpoint permite listar, criar, atualizar e excluir murais de avisos.
    """
    queryset = MuralAvisos.objects.all()
    serializer_class = MuralAvisosSerializer
    permission_classes = [
        CoordenadorFullPermission
    ]