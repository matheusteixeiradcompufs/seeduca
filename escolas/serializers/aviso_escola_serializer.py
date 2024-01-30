from rest_framework import serializers

from escolas.models import AvisoEscola


class AvisoEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvisoEscola
        fields = [
            'id',
            'titulo',
            'texto',
            'publicado_em',
            'mural',
        ]