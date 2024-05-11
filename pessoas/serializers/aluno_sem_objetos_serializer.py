from rest_framework import serializers
from pessoas.models import Aluno
from pessoas.serializers.usuario_serializer import UsuarioSerializer


class AlunoSemObjetosSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização de objetos Aluno, excluindo a serialização de objetos relacionados.
    """
    class Meta:
        model = Aluno
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'usuario',
            'endereco',
            'criado_em',
            'atualizado_em',
            'eh_pcd',
            'descricao_pcd',
            'retrato',
            'objeto_usuario',
        ]

    objeto_usuario = UsuarioSerializer(
        many=False,
        source='usuario',
        read_only=True,
    )
