from rest_framework import viewsets

from pessoas.models import Recado
from pessoas.permissions import AlunoPermission
from pessoas.serializers import RecadoSerializer


class RecadoViewSet(viewsets.ModelViewSet):
    queryset = Recado.objects.all()
    serializer_class = RecadoSerializer
    permission_classes = [
        # AlunoPermission,
    ]