from rest_framework import viewsets

from pessoas.models import DiaLetivo
from pessoas.permissions import ProfessorCreateUpdatePermission
from pessoas.serializers import DiaLetivoSerializer


class DiaLetivoViewSet(viewsets.ModelViewSet):
    queryset = DiaLetivo.objects.all()
    serializer_class = DiaLetivoSerializer
    permission_classes = [
        ProfessorCreateUpdatePermission,
    ]