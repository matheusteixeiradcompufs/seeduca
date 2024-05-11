from rest_framework import serializers
from escolas.models import CardapioMerenda
from escolas.serializers.item_cardapio_serializer import ItemCardapioMerendaSerializer


class CardapioMerendaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model CardapioMerenda.

    Este serializer é usado para serializar/desserializar instâncias de CardapioMerenda.
    Ele inclui o relacionamento com a model ItemCardapioMerendaSerializer para serialização de objetos itens.

    Atributos:
        id (int): O identificador único do cardápio de merenda.
        data (date): A data para a qual o cardápio está programado.
        turno (str): O turno ao qual o cardápio está associado.
        itens (list): Uma lista de itens de cardápio associados ao cardápio de merenda.
        escola (int): O identificador único da escola associada ao cardápio.
        objetos_itens (list): Uma lista de objetos itens associados ao cardápio de merenda.
    """
    class Meta:
        model = CardapioMerenda
        fields = [
            'id',
            'data',
            'turno',
            'itens',
            'escola',
            'objetos_itens',
        ]

    objetos_itens = ItemCardapioMerendaSerializer(
        many=True,
        source='itens',
        read_only=True,
    )
