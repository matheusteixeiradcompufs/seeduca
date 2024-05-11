from rest_framework import serializers
from pessoas.models import Frequencia
from pessoas.serializers.dia_letivo_serializer import DiaLetivoSerializer


class FrequenciaSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Frequencia.
    """

    class Meta:
        model = Frequencia
        fields = [
            'id',
            'percentual',
            'boletim',
            'objetos_diasletivos',
        ]

    objetos_diasletivos = DiaLetivoSerializer(
        many=True,
        source='frequencia_diasletivos',
        read_only=True,
    )
