from rest_framework import serializers
from pessoas.models import Transporte
from pessoas.serializers.aluno_sem_objetos_serializer import AlunoSemObjetosSerializer
from pessoas.serializers.telefone_transporte_serializer import TelefoneTransporteSerializer


class TransporteSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Transporte.
    """

    class Meta:
        model = Transporte
        fields = [
            'id',  # ID do transporte
            'placa',  # Placa do veículo
            'ano',  # Ano do veículo
            'tipo',  # Tipo do veículo
            'nomeMotorista',  # Nome do motorista
            'nomeAuxiliar',  # Nome do auxiliar
            'itinerario',  # Itinerário do transporte
            'criado_em',  # Data de criação do registro
            'atualizado_em',  # Data de atualização do registro
            'alunos',  # Alunos associados ao transporte
            'objetos_telefones',  # Telefones associados ao transporte
            'objetos_alunos',  # Objetos serializados dos alunos associados
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
