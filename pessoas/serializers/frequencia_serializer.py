from rest_framework import serializers

from pessoas.models import Frequencia
from pessoas.serializers.dia_letivo_serializer import DiaLetivoSerializer


class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencia
        fields = [
            'id',
            'percentual',
            'objetos_diasletivos',
        ]
    objetos_diasletivos = DiaLetivoSerializer(
        many=True,
        source='frequencia_diasletivos',
        read_only=True,
    )