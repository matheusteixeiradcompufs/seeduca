from rest_framework import serializers

from escolas.models import Escola, Telefone, Email


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = [
            'id',
            'numero',
        ]


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = [
            'id',
            'endereco',
        ]


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = [
            'id',
            'cnpj',
            'nome',
            'endereco',
            'num_salas',
            'descricao',
            'criado_em',
            'atualizado_em',
            'imagem',
            'objetos_telefones',
            'objetos_emails',
        ]
    objetos_telefones = TelefoneSerializer(
        many=True,
        source='telefones',
        read_only=True,
    )
    objetos_emails = EmailSerializer(
        many=True,
        source='emails',
        read_only=True,
    )