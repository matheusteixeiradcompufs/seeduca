from rest_framework import serializers
from pessoas.models import AgendaRecados
from pessoas.serializers.recado_serializer import RecadoSerializer


class AgendaRecadosSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos AgendaRecados.
    """
    class Meta:
        model = AgendaRecados
        fields = [
            'id',
            'boletim',
            'objetos_recados',
        ]

    objetos_recados = RecadoSerializer(
        many=True,
        source='agenda_recados',
        read_only=True,
    )
