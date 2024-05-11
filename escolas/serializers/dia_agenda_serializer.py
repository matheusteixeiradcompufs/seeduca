from rest_framework import serializers
from escolas.models import DiaAgenda
from escolas.serializers.disciplina_serializer import DisciplinaSerializer
from escolas.serializers.aviso_serializer import AvisoSerializer
from escolas.serializers.tarefa_serializer import TarefaSerializer


class DiaAgendaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model DiaAgenda.

    Este serializer é usado para serializar/desserializar instâncias de DiaAgenda.
    Ele inclui os relacionamentos com as models DisciplinaSerializer, AvisoSerializer e TarefaSerializer
    para serialização de disciplinas, avisos e tarefas associadas ao dia da agenda.

    Atributos:
        id (int): O identificador único do dia da agenda.
        data (date): A data do dia da agenda.
        util (bool): Indica se o dia é útil.
        disciplinas (list): Uma lista de disciplinas associadas ao dia da agenda.
        agenda (int): O identificador único da agenda escolar associada ao dia da agenda.
        criado_em (datetime): A data e hora de criação do dia da agenda.
        atualizado_em (datetime): A data e hora da última atualização do dia da agenda.
        objetos_disciplinas (list): Uma lista de objetos disciplinas associadas ao dia da agenda.
        objetos_avisos (list): Uma lista de objetos avisos associados ao dia da agenda.
        objetos_tarefas (list): Uma lista de objetos tarefas associadas ao dia da agenda.
    """
    class Meta:
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

    objetos_disciplinas = DisciplinaSerializer(
        many=True,
        source='disciplinas',
        read_only=True,
    )
    objetos_avisos = AvisoSerializer(
        many=True,
        source='dia_avisos',
        read_only=True,
    )
    objetos_tarefas = TarefaSerializer(
        many=True,
        source='dia_tarefas',
        read_only=True,
    )
