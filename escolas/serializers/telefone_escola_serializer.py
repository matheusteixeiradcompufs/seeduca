from rest_framework import serializers
from escolas.models import TelefoneEscola


class TelefoneEscolaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model TelefoneEscola.

    Este serializer é usado para serializar/desserializar instâncias de TelefoneEscola.

    Atributos:
        id (int): O identificador único do telefone da escola.
        numero (str): O número de telefone da escola.
        escola (int): O identificador único da escola associada ao telefone.
    """
    class Meta:
        model = TelefoneEscola
        fields = [
            'id',
            'numero',
            'escola',
        ]
