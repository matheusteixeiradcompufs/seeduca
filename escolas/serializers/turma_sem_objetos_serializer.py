from rest_framework import serializers

from escolas.models import Turma
from escolas.serializers.sala_sem_turma_serializer import SalaSemTurmaSerializer


class TurmaSemObjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = [
            'id',
            'nome',
            'ano',
            'turno',
            'criada_em',
            'atualizada_em',
            'sala',
            'disciplinas',
            'objeto_sala',
        ]

    objeto_sala = SalaSemTurmaSerializer(
        many=False,
        source='sala',
        read_only=True,
    )