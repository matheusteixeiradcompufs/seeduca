from rest_framework import serializers

from escolas.models import AgendaEscolar
from escolas.serializers.dia_agenda_serializer import DiaAgendaSerializer


class AgendaEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaEscolar
        fields = [
            'id',
            'turma',
            'objetos_dias',
        ]
    objetos_dias = DiaAgendaSerializer(
        many=True,
        source='agenda_dias',
        read_only=True,
    )