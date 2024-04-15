from rest_framework import serializers

from pessoas.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'endereco',
            'uid',
            'token',
            'criado_em',
            'atualizado_em',
            'usuario',
        ]