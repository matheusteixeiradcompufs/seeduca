from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from pessoas.models import Recado
from pessoas.serializers import RecadoSerializer


class RecadoViewSet(viewsets.ModelViewSet):
    queryset = Recado.objects.all()
    serializer_class = RecadoSerializer
    permission_classes = [
        AllowAny,
    ]