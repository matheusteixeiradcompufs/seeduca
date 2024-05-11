from rest_framework import serializers
from pessoas.models import DiaLetivo


class DiaLetivoSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos DiaLetivo.
    """
    class Meta:
        model = DiaLetivo
        fields = [
            'id',
            'data',
            'presenca',
            'criado_em',
            'atualizado_em',
            'frequencia',
        ]
