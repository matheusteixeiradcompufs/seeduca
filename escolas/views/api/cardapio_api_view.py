from rest_framework import viewsets

from escolas.models import CardapioMerenda
from escolas.serializers import CardapioMerendaSerializer
from pessoas.permissions import CoordenadorFullPermission


class CardapioMerendaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação dos cardápios de uma escola.

    Este endpoint permite listar, criar, atualizar e excluir cardápios.
    """
    queryset = CardapioMerenda.objects.all()
    serializer_class = CardapioMerendaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]