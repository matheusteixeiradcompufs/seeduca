from rest_framework import serializers
from escolas.models import AgendaEscolar
from escolas.serializers.app.app_dia_agenda_serializer import AppDiaAgendaSerializer


class AppAgendaEscolarSerializer(serializers.ModelSerializer):
    """
    Serializer para a agenda escolar de uma turma. Exclusivo para a API Restful do app mobile.

    Esta classe é responsável por serializar os dados da agenda escolar de uma escola,
    incluindo informações sobre a turma e os objetos relacionados aos dias da agenda.
    """

    class Meta:
        """
        Metaclasse que define os metadados do serializer.

        Atributos:
            model (Model): O modelo de dados a ser serializado.
            fields (list): Lista dos campos do modelo a serem incluídos na serialização.
        """
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
