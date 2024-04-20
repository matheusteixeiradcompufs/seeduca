from rest_framework import serializers

from escolas.models import Sala
from escolas.serializers.turma_sem_objetos_serializer import TurmaSemObjetosSerializer


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = [
            'id',
            'numero',
            'quantidade_alunos',
            'escola',
            'criado_em',
            'atualizado_em',
            'objetos_turmas',
        ]

    objetos_turmas = TurmaSemObjetosSerializer(
        many=True,
        source='sala_turmas',
        read_only=True,
    )