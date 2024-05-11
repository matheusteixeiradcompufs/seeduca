from rest_framework import serializers
from escolas.models import ItemCardapioMerenda


class ItemCardapioMerendaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model ItemCardapioMerenda.

    Este serializer é usado para serializar/desserializar instâncias de ItemCardapioMerenda.

    Atributos:
        id (int): O identificador único do item do cardápio de merenda.
        nome (str): O nome do item do cardápio de merenda.
        descricao (str): A descrição do item do cardápio de merenda.
        criado_em (datetime): A data e hora de criação do item do cardápio de merenda.
        atualizado_em (datetime): A data e hora da última atualização do item do cardápio de merenda.
    """
    class Meta:
        model = ItemCardapioMerenda
        fields = [
            'id',
            'nome',
            'descricao',
            'criado_em',
            'atualizado_em',
        ]
