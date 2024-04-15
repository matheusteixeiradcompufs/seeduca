from rest_framework import viewsets

from escolas.models import ItemCardapioMerenda
from escolas.serializers import ItemCardapioMerendaSerializer
from pessoas.permissions import CoordenadorFullPermission


class ItemCardapioMerendaViewSet(viewsets.ModelViewSet):
    queryset = ItemCardapioMerenda.objects.all()
    serializer_class = ItemCardapioMerendaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]