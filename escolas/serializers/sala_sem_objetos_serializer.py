from rest_framework import serializers

from escolas.models import Sala


class SalaSemObjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = [
            'id',
            'numero',
            'quantidade_alunos',
            'escola',
            'criado_em',
            'atualizado_em',
        ]