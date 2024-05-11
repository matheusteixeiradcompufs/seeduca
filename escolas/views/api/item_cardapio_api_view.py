from rest_framework import viewsets

from escolas.models import ItemCardapioMerenda
from escolas.serializers import ItemCardapioMerendaSerializer
from pessoas.permissions import CoordenadorFullPermission


class ItemCardapioMerendaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de itens de cardápio.

    Este endpoint permite listar, criar, atualizar e excluir itens de cardápio.
    """
    queryset = ItemCardapioMerenda.objects.all()
    serializer_class = ItemCardapioMerendaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]