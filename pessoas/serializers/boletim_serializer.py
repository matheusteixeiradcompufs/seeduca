from rest_framework import serializers

from pessoas.models import Boletim
from pessoas.serializers.avaliacao_serializer import AvaliacaoSerializer


class BoletimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletim
        fields = [
            'id',
            'ano',
            'aluno',
            'objetos_avaliacoes',
        ]

    objetos_avaliacoes = AvaliacaoSerializer(
        many=True,
        source='boletim_avaliacoes',
        read_only=True,
    )