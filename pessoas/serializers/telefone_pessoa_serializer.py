from rest_framework import serializers
from pessoas.models import TelefonePessoa


class TelefonePessoaSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos TelefonePessoa.
    """
    class Meta:
        model = TelefonePessoa
        fields = [
            'id',           # ID do telefone
            'numero',       # Número de telefone
            'pessoa',       # Pessoa associada ao telefone
        ]
