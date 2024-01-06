from rest_framework import serializers

from escolas.models import Aviso


class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = [
            'id',
            'titulo',
            'texto',
            'publicado_em',
            'diaAgenda',
        ]