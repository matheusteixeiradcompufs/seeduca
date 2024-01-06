from rest_framework import serializers

from escolas.models import CardapioMerenda
from escolas.serializers.item_cardapio_serializer import ItemCardapioMerendaSerializer


class CardapioMerendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardapioMerenda
        fields = [
            'id',
            'data',
            'turno',
            'item',
            'escola',
            'objetos_itens',
        ]
    objetos_itens = ItemCardapioMerendaSerializer(
        many=True,
        source='item',
        read_only=True,
    )