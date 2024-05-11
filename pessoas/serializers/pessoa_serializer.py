from rest_framework import serializers
from pessoas.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Pessoa.
    """
    class Meta:
        model = Pessoa
        fields = [
            'id',                   # ID da pessoa
            'matricula',            # Matrícula da pessoa
            'cpf',                  # CPF da pessoa
            'data_nascimento',      # Data de nascimento da pessoa
            'endereco',             # Endereço da pessoa
            'uid',                  # UID da pessoa
            'token',                # Token da pessoa
            'criado_em',            # Data de criação do registro
            'atualizado_em',        # Data de atualização do registro
            'usuario',              # Usuário associado à pessoa
        ]
