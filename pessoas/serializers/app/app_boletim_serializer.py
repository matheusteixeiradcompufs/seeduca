from rest_framework import serializers

from escolas.serializers.app.app_turma_serializer import AppTurmaSerializer
from pessoas.models import Boletim
from pessoas.serializers.app.app_agenda_recado_serializer import AppAgendaRecadosSerializer
from pessoas.serializers.frequencia_serializer import FrequenciaSerializer
from pessoas.serializers.avaliacao_serializer import AvaliacaoSerializer
from pessoas.serializers.media_serializer import MediaSerializer
from pessoas.serializers.situacao_serializer import SituacaoSerializer


class AppBoletimSerializer(serializers.ModelSerializer):
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
