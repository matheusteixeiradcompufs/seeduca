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
            'finalizada',
            'criada_em',
            'atualizada_em',
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
