from rest_framework import serializers

from pessoas.models import AgendaRecados
from pessoas.serializers.recado_serializer import RecadoSerializer


class AgendaRecadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaRecados
        fields = [
            'id',
            'ano',
            'aluno',
            'objetos_recados',
        ]

    objetos_recados = RecadoSerializer(
        many=True,
        source='agenda_recados',
        read_only=True,
    )