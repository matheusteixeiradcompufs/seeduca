from rest_framework import serializers

from escolas.serializers import DisciplinaSerializer
from pessoas.models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            'id',
            'tipo',
            'valor',
            'criada_em',
            'atualizada_em',
            'disciplina',
            'boletim',
            'objeto_disciplina',
        ]

    objeto_disciplina = DisciplinaSerializer(
        many=False,
        source='disciplina',
        read_only=True,
    )