from rest_framework import serializers
from escolas.models import DiaAgenda
from escolas.serializers.app.app_aviso_serializer import AppAvisoSerializer
from escolas.serializers.app.app_tarefa_serializer import AppTarefaSerializer
from escolas.serializers.disciplina_serializer import DisciplinaSerializer


class AppDiaAgendaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo DiaAgenda. Exclusivo para a API Restful do app mobile.

    Este serializer é usado para serializar/deserializar objetos DiaAgenda,
    permitindo sua representação em JSON para uso em APIs.

    Attributes:
        id (int): O identificador único do dia na agenda.
        data (datetime): A data do dia na agenda.
        util (bool): Indica se o dia é útil (True) ou não (False).
        disciplinas (list): Lista de disciplinas associadas ao dia na agenda.
        agenda (int): O identificador único da agenda à qual o dia pertence.
        criado_em (datetime): A data e hora de criação do registro.
        atualizado_em (datetime): A data e hora da última atualização do registro.
        objetos_disciplinas (list): Lista de objetos serializados de disciplinas associadas ao dia.
        objetos_avisos (list): Lista de objetos serializados de avisos associados ao dia.
        objetos_tarefas (list): Lista de objetos serializados de tarefas associadas ao dia.
    """
    objetos_disciplinas = DisciplinaSerializer(
        many=True,
        source='disciplinas',
        read_only=True,
    )
    objetos_avisos = AppAvisoSerializer(
        many=True,
        source='dia_avisos',
        read_only=True,
    )
    objetos_tarefas = AppTarefaSerializer(
        many=True,
        source='dia_tarefas',
        read_only=True,
    )

    class Meta:
        """
        Metaclasse do Serializer.

        Define os metadados do Serializer, incluindo o modelo associado e os
        campos a serem incluídos na serialização.

        Attributes:
            model (Model): O modelo associado ao Serializer (DiaAgenda).
            fields (list): Lista de campos do modelo a serem incluídos na serialização.
        """
        model = DiaAgenda
        fields = [
            'id',
            'data',
            'util',
            'disciplinas',
            'agenda',
            'criado_em',
            'atualizado_em',
            'objetos_disciplinas',
            'objetos_avisos',
            'objetos_tarefas',
        ]
