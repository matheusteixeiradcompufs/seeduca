from rest_framework import serializers
from escolas.models import MuralAvisos
from escolas.serializers.aviso_escola_serializer import AvisoEscolaSerializer


class MuralAvisosSerializer(serializers.ModelSerializer):
    """
    Serializer para a model MuralAvisos.

    Este serializer é usado para serializar/desserializar instâncias de MuralAvisos.
    Ele inclui o relacionamento com a model AvisoEscolaSerializer para serialização de avisos associados ao mural.

    Atributos:
        id (int): O identificador único do mural de avisos.
        ano (int): O ano ao qual o mural de avisos está associado.
        escola (int): O identificador único da escola associada ao mural de avisos.
        objetos_avisos (list): Uma lista de objetos avisos associados ao mural de avisos.
    """
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
