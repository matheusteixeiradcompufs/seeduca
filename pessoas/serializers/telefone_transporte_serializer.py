from rest_framework import serializers
from pessoas.models import TelefoneTransporte


class TelefoneTransporteSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos TelefoneTransporte.
    """
    class Meta:
        model = TelefoneTransporte
        fields = [
            'id',           # ID do telefone
            'numero',       # Número de telefone
            'transporte',   # Transporte associado ao telefone
        ]
