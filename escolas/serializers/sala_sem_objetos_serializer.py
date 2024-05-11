from rest_framework import serializers
from escolas.models import Sala


class SalaSemObjetosSerializer(serializers.ModelSerializer):
    """
    Serializer para a model Sala.

    Este serializer é usado para serializar/desserializar instâncias de Sala.
    Ele não inclui relacionamentos com outras models.

    Atributos:
        id (int): O identificador único da sala.
        numero (int): O número da sala.
        quantidade_alunos (int): A quantidade de alunos na sala.
        escola (int): O identificador único da escola associada à sala.
        criado_em (datetime): A data e hora de criação da sala.
        atualizado_em (datetime): A data e hora da última atualização da sala.
    """
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
