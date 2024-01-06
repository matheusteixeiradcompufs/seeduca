from rest_framework import viewsets

from pessoas.models import Avaliacao
from pessoas.permissions import ProfessorUpdatePermission
from pessoas.serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [
        ProfessorUpdatePermission,
    ]