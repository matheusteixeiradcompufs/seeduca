from rest_framework import viewsets

from escolas.models import Turma
from escolas.serializers import TurmaSerializer
from pessoas.permissions import CoordenadorFullPermission


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [
        # CoordenadorFullPermission,
    ]