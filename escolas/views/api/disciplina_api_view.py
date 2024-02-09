from rest_framework import viewsets

from escolas.models import Disciplina
from escolas.serializers import DisciplinaSerializer
from pessoas.permissions import CoordenadorFullPermission


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [
        # CoordenadorFullPermission,
    ]