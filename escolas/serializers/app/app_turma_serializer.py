from rest_framework import serializers
from escolas.models import Turma
from escolas.serializers import SalaSemTurmaSerializer
from escolas.serializers.app.app_agenda_escola_serializer import AppAgendaEscolarSerializer
from escolas.serializers.disciplina_serializer import DisciplinaSerializer


class AppTurmaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Turma. Exclusivo para a API Restful do app mobile.

    Este serializer é usado para serializar/deserializar objetos Turma,
    permitindo sua representação em JSON para uso em APIs.

    Attributes:
        id (int): O identificador único da turma.
        nome (str): O nome da turma.
        ano (int): O ano associado à turma.
        turno (str): O turno da turma.
        criada_em (datetime): A data e hora de criação da turma.
        atualizada_em (datetime): A data e hora da última atualização da turma.
        sala (int): O identificador único da sala associada à turma.
        disciplinas (list): Lista de disciplinas associadas à turma.
        objeto_agenda (dict): Objeto serializado da agenda escolar associada à turma.
        objetos_disciplinas (list): Lista de objetos serializados de disciplinas associadas à turma.
        objeto_sala (dict): Objeto serializado da sala associada à turma.
    """
    objeto_agenda = AppAgendaEscolarSerializer(
        many=False,
        source='turma_agenda',
        read_only=True,
    )
    objetos_disciplinas = DisciplinaSerializer(
        many=True,
        source='disciplinas',
        read_only=True,
    )
    objeto_sala = SalaSemTurmaSerializer(
        many=False,
        source='sala',
        read_only=True,
    )

    class Meta:
        """
        Metaclasse do Serializer.

        Define os metadados do Serializer, incluindo o modelo associado e os
        campos a serem incluídos na serialização.

        Attributes:
            model (Model): O modelo associado ao Serializer (Turma).
            fields (list): Lista de campos do modelo a serem incluídos na serialização.
        """
        model = Turma
        fields = [
            'id',
            'nome',
            'ano',
            'turno',
            'criada_em',
            'atualizada_em',
            'sala',
            'disciplinas',
            'objeto_agenda',
            'objetos_disciplinas',
            'objeto_sala',
        ]
