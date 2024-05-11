from rest_framework import serializers
from escolas.models import Turma
from escolas.serializers.agenda_escola_serializer import AgendaEscolarSerializer
from escolas.serializers.disciplina_serializer import DisciplinaSerializer
from escolas.serializers.sala_sem_turma_serializer import SalaSemTurmaSerializer
from pessoas.serializers.boletim_sem_objetos_serializer import BoletimSemObjetosSerializer


class TurmaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model Turma.

    Este serializer é usado para serializar/desserializar instâncias de Turma.
    Ele inclui os relacionamentos com as models AgendaEscolarSerializer, DisciplinaSerializer,
    SalaSemTurmaSerializer e BoletimSemObjetosSerializer para serialização de informações sobre
    agenda, disciplinas, boletins e sala associadas à turma.

    Atributos:
        id (int): O identificador único da turma.
        nome (str): O nome da turma.
        ano (int): O ano da turma.
        turno (str): O turno da turma.
        criada_em (datetime): A data e hora de criação da turma.
        atualizada_em (datetime): A data e hora da última atualização da turma.
        sala (int): O identificador único da sala associada à turma.
        disciplinas (list): Uma lista de informações sobre as disciplinas associadas à turma.
        objeto_agenda (dict): As informações sobre a agenda da turma.
        objetos_disciplinas (list): Uma lista de informações sobre as disciplinas associadas à turma.
        objetos_boletins (list): Uma lista de informações sobre os boletins associados à turma.
        objeto_sala (dict): As informações sobre a sala associada à turma.
    """
    class Meta:
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
            'objetos_boletins',
            'objeto_sala',
        ]

    objeto_agenda = AgendaEscolarSerializer(
        many=False,
        source='turma_agenda',
        read_only=True,
    )
    objetos_disciplinas = DisciplinaSerializer(
        many=True,
        source='disciplinas',
        read_only=True,
    )
    objetos_boletins = BoletimSemObjetosSerializer(
        many=True,
        source='turma_boletins',
        read_only=True,
    )
    objeto_sala = SalaSemTurmaSerializer(
        many=False,
        source='sala',
        read_only=True,
    )
