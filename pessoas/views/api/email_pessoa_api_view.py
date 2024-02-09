from rest_framework import viewsets

from pessoas.models import EmailPessoa
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import EmailPessoaSerializer


class EmailPessoaViewSet(viewsets.ModelViewSet):
    queryset = EmailPessoa.objects.all()
    serializer_class = EmailPessoaSerializer
    permission_classes = [
        # CoordenadorFullPermission,
    ]