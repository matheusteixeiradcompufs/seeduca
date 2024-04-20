from rest_framework import serializers

from escolas.models import AgendaEscolar
from escolas.serializers.app.app_dia_agenda_serializer import AppDiaAgendaSerializer
from escolas.serializers.dia_agenda_serializer import DiaAgendaSerializer


class AppAgendaEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaEscolar
        fields = [
            'id',
            'turma',
            'objetos_dias',
        ]
    objetos_dias = AppDiaAgendaSerializer(
        many=True,
        source='agenda_dias',
        read_only=True,
    )