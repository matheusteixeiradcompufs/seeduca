from rest_framework import serializers
from escolas.models import Sala
from escolas.serializers.turma_sem_objetos_serializer import TurmaSemObjetosSerializer


class SalaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model Sala.

    Este serializer é usado para serializar/desserializar instâncias de Sala.
    Ele inclui o relacionamento com a model TurmaSemObjetosSerializer para serialização de informações sobre turmas associadas à sala.

    Atributos:
        id (int): O identificador único da sala.
        numero (int): O número da sala.
        quantidade_alunos (int): A quantidade de alunos na sala.
        escola (int): O identificador único da escola associada à sala.
        criado_em (datetime): A data e hora de criação da sala.
        atualizado_em (datetime): A data e hora da última atualização da sala.
        objetos_turmas (list): Uma lista de informações sobre turmas associadas à sala.
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
            'objetos_turmas',
        ]

    objetos_turmas = TurmaSemObjetosSerializer(
        many=True,
        source='sala_turmas',
        read_only=True,
    )
