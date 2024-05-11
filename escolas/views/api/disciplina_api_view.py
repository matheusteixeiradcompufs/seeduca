from rest_framework import viewsets

from escolas.models import Disciplina
from escolas.serializers import DisciplinaSerializer
from pessoas.permissions import CoordenadorFullPermission


class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de disciplinas.

    Este endpoint permite listar, criar, atualizar e excluir disciplinas.
    """
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]