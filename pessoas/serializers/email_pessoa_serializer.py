from rest_framework import serializers
from pessoas.models import EmailPessoa


class EmailPessoaSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos EmailPessoa.
    """
    class Meta:
        model = EmailPessoa
        fields = [
            'id',
            'endereco',
            'pessoa',
        ]
