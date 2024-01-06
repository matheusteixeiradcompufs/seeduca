from rest_framework import serializers

from pessoas.models import DiaLetivo


class DiaLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaLetivo
        fields = [
            'id',
            'data',
            'presenca',
            'frequencia',
        ]