from rest_framework import serializers

from escolas.models import DiaAgenda
from escolas.serializers.app.app_aviso_serializer import AppAvisoSerializer
from escolas.serializers.app.app_tarefa_serializer import AppTarefaSerializer
from escolas.serializers.disciplina_serializer import DisciplinaSerializer
from escolas.serializers.tarefa_serializer import TarefaSerializer


class AppDiaAgendaSerializer(serializers.ModelSerializer):
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
    objetos_avisos = AppAvisoSerializer(
        many=True,
        source='dia_avisos',
        read_only=True,
    )
    objetos_tarefas = AppTarefaSerializer(
        many=True,
        source='dia_tarefas',
        read_only=True,
    )