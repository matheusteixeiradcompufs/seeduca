from rest_framework import serializers
from escolas.models import Aviso


class AvisoSerializer(serializers.ModelSerializer):
    """
    Serializer para a model Aviso.

    Este serializer é usado para serializar/desserializar instâncias de Aviso.

    Atributos:
        id (int): O identificador único do aviso.
        titulo (str): O título do aviso.
        texto (str): O texto do aviso.
        publicado_em (datetime): A data e hora em que o aviso foi publicado.
        atualizado_em (datetime): A data e hora da última atualização do aviso.
        diaAgenda (int): O identificador único do dia da agenda ao qual o aviso está associado.
    """
    class Meta:
        model = Aviso
        fields = [
            'id',
            'titulo',
            'texto',
            'publicado_em',
            'atualizado_em',
            'diaAgenda',
        ]
