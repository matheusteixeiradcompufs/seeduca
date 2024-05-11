from rest_framework import serializers
from pessoas.models import AgendaRecados
from pessoas.serializers.recado_serializer import RecadoSerializer


class AppAgendaRecadosSerializer(serializers.ModelSerializer):
    """
    Serializer para a aplicação de agenda de recados. Exclusivo para a API Restful do app mobile.

    Esta classe serializa os dados da AgendaRecados e também inclui os recados associados.
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

# Observações:
# - 'id': O identificador único da agenda de recados.
# - 'boletim': O boletim associado à agenda de recados.
# - 'objetos_recados': Lista de recados associados à agenda de recados.
#                     Esta lista é fornecida pelo RecadoSerializer.
