from rest_framework import serializers

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
        ]