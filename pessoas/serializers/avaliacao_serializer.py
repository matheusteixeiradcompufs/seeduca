from rest_framework import serializers
from escolas.serializers import DisciplinaSerializer
from pessoas.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Avaliacao.
    """
    class Meta:
        model = Avaliacao
        fields = [
            'id',
            'nome',
            'nota',
            'confirmar',
            'criada_em',
            'atualizada_em',
            'aluno',
            'disciplina',
            'boletim',
            'objeto_disciplina',
        ]

    objeto_disciplina = DisciplinaSerializer(
        many=False,
        source='disciplina',
        read_only=True,
    )
