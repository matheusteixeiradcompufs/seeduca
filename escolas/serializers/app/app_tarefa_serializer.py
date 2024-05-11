from rest_framework import serializers
from escolas.models import Tarefa


class AppTarefaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Tarefa. Exclusivo para a API Restful do app mobile.

    Este serializer é usado para serializar/deserializar objetos Tarefa,
    permitindo sua representação em JSON para uso em APIs.

    Attributes:
        id (int): O identificador único da tarefa.
        nome (str): O nome da tarefa.
        descricao (str): A descrição da tarefa.
        tipo (str): O tipo de tarefa.
        cadastrada_em (datetime): A data e hora em que a tarefa foi cadastrada.
        atualizado_em (datetime): A data e hora da última atualização da tarefa.
        entrega (datetime): A data e hora de entrega da tarefa.
        diaAgenda (int): O identificador único do dia da agenda associado à tarefa.
    """
    class Meta:
        """
        Metaclasse do Serializer.

        Define os metadados do Serializer, incluindo o modelo associado e os
        campos a serem incluídos na serialização.

        Attributes:
            model (Model): O modelo associado ao Serializer (Tarefa).
            fields (list): Lista de campos do modelo a serem incluídos na serialização.
        """
        model = Tarefa
        fields = [
            'id',
            'nome',
            'descricao',
            'tipo',
            'cadastrada_em',
            'atualizado_em',
            'entrega',
            'diaAgenda',
        ]
