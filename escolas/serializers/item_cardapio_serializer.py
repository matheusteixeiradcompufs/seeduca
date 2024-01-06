from rest_framework import serializers

from escolas.models import ItemCardapioMerenda


class ItemCardapioMerendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCardapioMerenda
        fields = [
            'id',
            'nome',
            'descricao',
        ]