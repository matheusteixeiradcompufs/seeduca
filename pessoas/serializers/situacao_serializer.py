from rest_framework import serializers
from escolas.serializers import DisciplinaSerializer
from pessoas.models import Situacao


class SituacaoSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Situacao.
    """
    class Meta:
        model = Situacao
        fields = [
            'id',                   # ID da situação
            'situacao',             # Situação
            'finalizar',            # Indica se é para finalizar a situação
            'disciplina',           # Disciplina associada à situação
            'boletim',              # Boletim associado à situação
            'objeto_disciplina',    # Objeto serializado da disciplina associada
        ]

    objeto_disciplina = DisciplinaSerializer(
        many=False,
        source='disciplina',
        read_only=True,
    )
