from rest_framework import serializers

from escolas.models import TelefoneEscola


class TelefoneEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneEscola
        fields = [
            'id',
            'numero',
            'escola',
        ]