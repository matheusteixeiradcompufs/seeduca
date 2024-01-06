from rest_framework import serializers

from escolas.models import Sala
from escolas.serializers.turma_serializer import TurmaSerializer


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = [
            'id',
            'numero',
            'quantidade_alunos',
            'escola',
            'objetos_turmas',
        ]
    objetos_turmas = TurmaSerializer(
        many=True,
        source='sala_turmas',
        read_only=True,
    )