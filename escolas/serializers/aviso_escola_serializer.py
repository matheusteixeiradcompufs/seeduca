from rest_framework import serializers
from escolas.models import AvisoEscola


class AvisoEscolaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model AvisoEscola.

    Este serializer é usado para serializar/desserializar instâncias de AvisoEscola.

    Atributos:
        id (int): O identificador único do aviso.
        titulo (str): O título do aviso.
        texto (str): O texto do aviso.
        publicado_em (datetime): A data e hora em que o aviso foi publicado.
        atualizado_em (datetime): A data e hora da última atualização do aviso.
        mural (str): O mural ao qual o aviso está associado.
    """
    class Meta:
        model = AvisoEscola
        fields = [
            'id',
            'titulo',
            'texto',
            'publicado_em',
            'atualizado_em',
            'mural',
        ]
