from rest_framework import viewsets

from escolas.models import CardapioMerenda
from escolas.serializers import CardapioMerendaSerializer
from pessoas.permissions import CoordenadorFullPermission


class CardapioMerendaViewSet(viewsets.ModelViewSet):
    queryset = CardapioMerenda.objects.all()
    serializer_class = CardapioMerendaSerializer
    permission_classes = [
        # CoordenadorFullPermission,
    ]