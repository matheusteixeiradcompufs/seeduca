from rest_framework import serializers

from pessoas.models import Responsavel


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = [
            'id',
            'cpf',
            'nome',
            'observacao',
            'aluno',
        ]