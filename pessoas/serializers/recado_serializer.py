from rest_framework import serializers
from pessoas.models import Recado


class RecadoSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Recado.
    """
    class Meta:
        model = Recado
        fields = [
            'id',               # ID do recado
            'texto',            # Texto do recado
            'eh_aluno',         # Indica se o remetente é um aluno
            'publicado_em',     # Data de publicação do recado
            'atualizado_em',    # Data de atualização do recado
            'pessoa',           # Pessoa remetente do recado
            'agenda',           # Agenda associada ao recado (opcional)
        ]
