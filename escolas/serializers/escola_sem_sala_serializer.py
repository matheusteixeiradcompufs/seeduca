from rest_framework import serializers

from escolas.models import Escola
from escolas.serializers.email_escola_serializer import EmailEscolaSerializer
from escolas.serializers.telefone_escola_serializer import TelefoneEscolaSerializer


class EscolaSemSalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = [
            'id',
            'cnpj',
            'nome',
            'endereco',
            'num_salas',
            'quantidade_alunos',
            'descricao',
            'criado_em',
            'atualizado_em',
            'imagem',
            'escola_telefones',
            'escola_emails',
        ]
    objetos_telefones = TelefoneEscolaSerializer(
        many=True,
        source='escola_telefones',
        read_only=True,
    )
    objetos_emails = EmailEscolaSerializer(
        many=True,
        source='escola_emails',
        read_only=True,
    )