from rest_framework import serializers
from escolas.models import Disciplina


class DisciplinaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model Disciplina.

    Este serializer é usado para serializar/desserializar instâncias de Disciplina.

    Atributos:
        id (int): O identificador único da disciplina.
        nome (str): O nome da disciplina.
    """
    class Meta:
        model = Disciplina
        fields = [
            'id',
            'nome',
        ]
