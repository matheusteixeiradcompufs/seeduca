from rest_framework import serializers

from escolas.models import MuralAvisos
from escolas.serializers.aviso_escola_serializer import AvisoEscolaSerializer


class MuralAvisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuralAvisos
        fields = [
            'id',
            'ano',
            'escola',
            'objetos_avisos',
        ]

    objetos_avisos = AvisoEscolaSerializer(
        many=True,
        source='mural_avisos',
        read_only=True
    )

