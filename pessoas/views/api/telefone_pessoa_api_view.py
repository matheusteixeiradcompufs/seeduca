from rest_framework import viewsets

from pessoas.models import TelefonePessoa
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import TelefonePessoaSerializer


class TelefonePessoaViewSet(viewsets.ModelViewSet):
    queryset = TelefonePessoa.objects.all()
    serializer_class = TelefonePessoaSerializer
    permission_classes = [
        # CoordenadorFullPermission,
    ]