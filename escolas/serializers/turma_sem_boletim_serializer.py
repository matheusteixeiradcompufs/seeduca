from rest_framework import serializers

from escolas.models import Turma
from escolas.serializers.agenda_escola_serializer import AgendaEscolarSerializer
from escolas.serializers.disciplina_serializer import DisciplinaSerializer
from pessoas.serializers import BoletimSerializer


class TurmaSerializer(serializers.ModelSerializer):
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
            'turma_boletins',
            'disciplinas',
            'objeto_agenda',
            'objetos_disciplinas',
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
    objetos_boletins = BoletimSerializer(
        many=True,
        source='turma_boletins',
        read_only=True,
    )