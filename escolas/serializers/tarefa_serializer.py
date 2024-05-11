from rest_framework import serializers
from escolas.models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model Tarefa.

    Este serializer é usado para serializar/desserializar instâncias de Tarefa.

    Atributos:
        id (int): O identificador único da tarefa.
        nome (str): O nome da tarefa.
        descricao (str): A descrição da tarefa.
        tipo (str): O tipo da tarefa.
        cadastrada_em (datetime): A data e hora de cadastro da tarefa.
        atualizado_em (datetime): A data e hora da última atualização da tarefa.
        entrega (date): A data de entrega da tarefa.
        diaAgenda (int): O identificador único do dia da agenda associado à tarefa.
    """
    class Meta:
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
