from rest_framework import serializers

from pessoas.models import EmailPessoa


class EmailPessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailPessoa
        fields = [
            'id',
            'endereco',
            'pessoa',
        ]