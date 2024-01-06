from rest_framework import serializers

from escolas.models import DiaAgenda
from escolas.serializers.aviso_serializer import AvisoSerializer
from escolas.serializers.tarefa_serializer import TarefaSerializer


class DiaAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaAgenda
        fields = [
            'id',
            'data',
            'disciplina',
            'agenda',
            'objetos_avisos',
            'objetos_tarefas',
        ]
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