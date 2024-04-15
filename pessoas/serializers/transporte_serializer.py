from rest_framework import serializers

from pessoas.models import Transporte
from pessoas.serializers.aluno_sem_objetos_serializer import AlunoSemObjetosSerializer
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
            'alunos',
            'objetos_telefones',
            'objetos_alunos',
        ]
    objetos_telefones = TelefoneTransporteSerializer(
        many=True,
        source='transporte_telefones',
        read_only=True,
    )
    objetos_alunos = AlunoSemObjetosSerializer(
        many=True,
        source='alunos',
        read_only=True,
    )