from rest_framework import serializers
from pessoas.models import Responsavel


class ResponsavelSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Responsavel.
    """
    class Meta:
        model = Responsavel
        fields = [
            'id',           # ID do responsável
            'cpf',          # CPF do responsável
            'nome',         # Nome do responsável
            'observacao',   # Observação sobre o responsável
            'aluno',        # Aluno associado ao responsável
        ]
