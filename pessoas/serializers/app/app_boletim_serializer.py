from rest_framework import serializers

from escolas.serializers.app.app_turma_serializer import AppTurmaSerializer
from pessoas.models import Boletim
from pessoas.serializers.app.app_agenda_recado_serializer import AppAgendaRecadosSerializer
from pessoas.serializers.frequencia_serializer import FrequenciaSerializer
from pessoas.serializers.avaliacao_serializer import AvaliacaoSerializer
from pessoas.serializers.media_serializer import MediaSerializer
from pessoas.serializers.situacao_serializer import SituacaoSerializer


class AppBoletimSerializer(serializers.ModelSerializer):
    """
        Serializer para a model Boletim. Exclusivo para a API Restful do app mobile.

        Este serializer é usado para serializar e desserializar instâncias da
        model Boletim. Ele inclui campos relacionados ao aluno, à turma, ao
        status do boletim, bem como informações sobre frequências, avaliações,
        médias, situações e agenda de recados associadas ao boletim.

        Fields:
            id (int): ID do boletim.
            aluno (int): ID do aluno associado ao boletim.
            status (str): Status do boletim.
            encerrar (bool): Indica se o boletim está encerrado.
            qr_code (str): URL do código QR associado ao boletim.
            turma (int): ID da turma associada ao boletim.
            objeto_turma (dict): Dados da turma associada ao boletim.
            objeto_frequencia (dict): Dados da frequência associada ao boletim.
            objetos_avaliacoes (list): Lista de avaliações associadas ao boletim.
            objetos_medias (list): Lista de médias associadas ao boletim.
            objetos_situacoes (list): Lista de situações associadas ao boletim.
            objeto_agenda (dict): Dados da agenda de recados associada ao boletim.
        """

    class Meta:
        model = Boletim
        fields = [
            'id',
            'aluno',
            'status',
            'encerrar',
            'qr_code',
            'turma',
            'objeto_turma',
            'objeto_frequencia',
            'objetos_avaliacoes',
            'objetos_medias',
            'objetos_situacoes',
            'objeto_agenda',
        ]

    objeto_frequencia = FrequenciaSerializer(
        many=False,
        source='boletim_frequencia',
        read_only=True,
    )
    objetos_avaliacoes = AvaliacaoSerializer(
        many=True,
        source='boletim_avaliacoes',
        read_only=True,
    )
    objetos_medias = MediaSerializer(
        many=True,
        source='boletim_medias',
        read_only=True,
    )
    objetos_situacoes = SituacaoSerializer(
        many=True,
        source='boletim_situacoes',
        read_only=True,
    )
    objeto_agenda = AppAgendaRecadosSerializer(
        many=False,
        source='boletim_agendas',
        read_only=True,
    )
    objeto_turma = AppTurmaSerializer(
        many=False,
        source='turma',
        read_only=True,
    )
