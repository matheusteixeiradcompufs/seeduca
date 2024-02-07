from rest_framework import serializers

from pessoas.models import Transporte
from pessoas.serializers.telefone_transporte_serializer import TelefoneTransporteSerializer


class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = [
            'id',
            'placa',
            'ano',
            'tipo',
            'nomeMotorista',
            'nomeAuxiliar',
            'itinerario',
            'criado_em',
            'atualizado_em',
            'aluno',
            'objetos_telefones',
        ]
    objetos_telefones = TelefoneTransporteSerializer(
        many=True,
        source='transporte_telefones',
        read_only=True,
    )