from rest_framework import serializers
from escolas.models import Sala
from escolas.serializers.escola_sem_sala_serializer import EscolaSemSalaSerializer


class SalaSemTurmaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model Sala.

    Este serializer é usado para serializar/desserializar instâncias de Sala sem incluir informações sobre turmas.
    Ele inclui o relacionamento com a model EscolaSemSalaSerializer para serialização de informações da escola associada à sala.

    Atributos:
        id (int): O identificador único da sala.
        numero (int): O número da sala.
        quantidade_alunos (int): A quantidade de alunos na sala.
        escola (int): O identificador único da escola associada à sala.
        criado_em (datetime): A data e hora de criação da sala.
        atualizado_em (datetime): A data e hora da última atualização da sala.
        objeto_escola (dict): As informações da escola associada à sala.
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
            'objeto_escola',
        ]

    objeto_escola = EscolaSemSalaSerializer(
        many=False,
        source='escola',
        read_only=True,
    )
