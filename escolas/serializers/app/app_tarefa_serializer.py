from rest_framework import serializers

from escolas.models import Tarefa


class AppTarefaSerializer(serializers.ModelSerializer):
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