from rest_framework import serializers

from escolas.models import Turma
from escolas.serializers.agenda_escola_serializer import AgendaEscolarSerializer
from escolas.serializers.disciplina_serializer import DisciplinaSerializer
from escolas.serializers.sala_sem_turma_serializer import SalaSemTurmaSerializer


class TurmaSemBoletimSerializer(serializers.ModelSerializer):
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
            'objeto_agenda',
            'objetos_disciplinas',
            'objeto_sala',
        ]

    objeto_agenda = AgendaEscolarSerializer(
        many=False,
        source='turma_agenda',
        read_only=True,
    )
    objetos_disciplinas = DisciplinaSerializer(
        many=True,
        source='disciplinas',
        read_only=True,
    )
    objeto_sala = SalaSemTurmaSerializer(
        many=False,
        source='sala',
        read_only=True,
    )