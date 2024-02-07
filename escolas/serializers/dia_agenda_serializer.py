from rest_framework import serializers

from escolas.models import DiaAgenda
from escolas.serializers.disciplina_serializer import DisciplinaSerializer
from escolas.serializers.aviso_serializer import AvisoSerializer
from escolas.serializers.tarefa_serializer import TarefaSerializer


class DiaAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaAgenda
        fields = [
            'id',
            'data',
            'util',
            'disciplinas',
            'agenda',
            'criado_em',
            'atualizado_em',
            'objetos_disciplinas',
            'objetos_avisos',
            'objetos_tarefas',
        ]
    objetos_disciplinas = DisciplinaSerializer(
        many=True,
        source='disciplinas',
        read_only=True,
    )
    objetos_avisos = AvisoSerializer(
        many=True,
        source='dia_avisos',
        read_only=True,
    )
    objetos_tarefas = TarefaSerializer(
        many=True,
        source='dia_tarefas',
        read_only=True,
    )