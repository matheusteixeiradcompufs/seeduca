from rest_framework import serializers
from escolas.models import AgendaEscolar
from escolas.serializers.dia_agenda_serializer import DiaAgendaSerializer


class AgendaEscolarSerializer(serializers.ModelSerializer):
    """
    Serializer para a model AgendaEscolar.

    Este serializer é usado para serializar/desserializar instâncias de AgendaEscolar.
    Ele inclui o relacionamento com a model DiaAgendaSerializer para serialização de objetos dias.

    Atributos:
        id (int): O identificador único da agenda escolar.
        turma (str): A turma associada à agenda escolar.
        objetos_dias (list): Uma lista de objetos dias associados à agenda escolar.
    """
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
