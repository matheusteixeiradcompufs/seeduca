from rest_framework import serializers

from escolas.serializers import TurmaSerializer
from pessoas.models import Boletim
from pessoas.serializers.frequencia_serializer import FrequenciaSerializer
from pessoas.serializers.avaliacao_serializer import AvaliacaoSerializer
from pessoas.serializers.media_serializer import MediaSerializer


class BoletimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletim
        fields = [
            'id',
            'ano',
            'aluno',
            'status',
            'encerrar',
            'frequencia',
            'turma',
            'objeto_turma',
            'objeto_frequencia',
            'objetos_avaliacoes',
            'objetos_medias',
        ]

    objeto_turma = TurmaSerializer(
        many=False,
        source='turma',
        read_only=True,
    )
    objeto_frequencia = FrequenciaSerializer(
        many=False,
        source='frequencia',
        read_only=True,
    )
    objetos_avaliacoes = AvaliacaoSerializer(
        many=True,
        source='boletim_avaliacoes',
        read_only=True,
    )
    objetos_medias = MediaSerializer(
        many=True,
        source='boletim_medias',
        read_only=True,
    )