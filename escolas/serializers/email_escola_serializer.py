from rest_framework import serializers
from escolas.models import EmailEscola


class EmailEscolaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model EmailEscola.

    Este serializer é usado para serializar/desserializar instâncias de EmailEscola.

    Atributos:
        id (int): O identificador único do e-mail da escola.
        endereco (str): O endereço de e-mail da escola.
        escola (int): O identificador único da escola associada ao e-mail.
    """
    class Meta:
        model = EmailEscola
        fields = [
            'id',
            'endereco',
            'escola',
        ]
