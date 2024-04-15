from rest_framework import serializers

from escolas.serializers import DisciplinaSerializer
from pessoas.models import Situacao


class SituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacao
        fields = [
            'id',
            'situacao',
            'finalizar',
            'disciplina',
            'boletim',
            'objeto_disciplina',
        ]

    objeto_disciplina = DisciplinaSerializer(
        many=False,
        source='disciplina',
        read_only=True,
    )