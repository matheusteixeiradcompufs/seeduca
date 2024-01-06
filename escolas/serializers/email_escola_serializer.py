from rest_framework import serializers

from escolas.models import EmailEscola


class EmailEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailEscola
        fields = [
            'id',
            'endereco',
            'escola',
        ]