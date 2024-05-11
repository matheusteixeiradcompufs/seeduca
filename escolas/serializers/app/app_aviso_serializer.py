from rest_framework import serializers
from escolas.models import Aviso


class AppAvisoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Aviso. Exclusivo para a API Restful do app mobile.

    Este serializer é usado para serializar/deserializar objetos Aviso,
    permitindo sua representação em JSON para uso em APIs.

    Attributes:
        id (int): O identificador único do aviso.
        titulo (str): O título do aviso.
        texto (str): O texto do aviso.
        publicado_em (datetime): A data e hora em que o aviso foi publicado.
        atualizado_em (datetime): A data e hora da última atualização do aviso.
        diaAgenda (datetime): A data e hora para o aviso em uma agenda específica.
    """
    class Meta:
        """
        Metaclasse do Serializer.

        Define os metadados do Serializer, incluindo o modelo associado e os
        campos a serem incluídos na serialização.

        Attributes:
            model (Model): O modelo associado ao Serializer (Aviso).
            fields (list): Lista de campos do modelo a serem incluídos na serialização.
        """
        model = Aviso
        fields = [
            'id',
            'titulo',
            'texto',
            'publicado_em',
            'atualizado_em',
            'diaAgenda',
        ]
