from rest_framework import serializers

from escolas.models import Escola


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
        ]