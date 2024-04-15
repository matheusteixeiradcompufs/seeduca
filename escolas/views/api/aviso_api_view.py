from rest_framework import viewsets

from escolas.models import Aviso
from escolas.serializers import AvisoSerializer
from pessoas.permissions import ProfessorCreateUpdatePermission


class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer
    permission_classes = [
        ProfessorCreateUpdatePermission,
    ]