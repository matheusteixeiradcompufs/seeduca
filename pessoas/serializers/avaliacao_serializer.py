from rest_framework import serializers

from escolas.serializers import DisciplinaSerializer
from pessoas.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = [
            'id',
            'nome',
            'nota',
            'aluno',
            'disciplina',
            'boletim',
            'turma',
            'objeto_disciplina',
        ]

    objeto_disciplina = DisciplinaSerializer(
        many=False,
        source='disciplina',
        read_only=True,
    )
