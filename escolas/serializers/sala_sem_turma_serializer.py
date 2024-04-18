from rest_framework import serializers

from escolas.models import Sala
from escolas.serializers.escola_sem_sala_serializer import EscolaSemSalaSerializer


class SalaSemTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = [
            'id',
            'numero',
            'quantidade_alunos',
            'escola',
            'criado_em',
            'atualizado_em',
            'objeto_escola',
        ]

    objeto_escola = EscolaSemSalaSerializer(
        many=False,
        source='escola',
        read_only=True,
    )