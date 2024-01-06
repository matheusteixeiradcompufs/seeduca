from rest_framework import serializers

from pessoas.models import TelefonePessoa


class TelefonePessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefonePessoa
        fields = [
            'id',
            'numero',
            'pessoa',
        ]