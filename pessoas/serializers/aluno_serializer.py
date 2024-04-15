from rest_framework import serializers

from pessoas.models import Aluno
from pessoas.serializers.telefone_pessoa_serializer import TelefonePessoaSerializer
from pessoas.serializers.email_pessoa_serializer import EmailPessoaSerializer
from pessoas.serializers.responsavel_serializer import ResponsavelSerializer
from pessoas.serializers.boletim_serializer import BoletimSerializer
from pessoas.serializers.transporte_serializer import TransporteSerializer
from pessoas.serializers.usuario_serializer import UsuarioSerializer


class AlunoSerializer(serializers.ModelSerializer):
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
            'objetos_telefones',
            'objetos_emails',
            'objetos_responsaveis',
            'objetos_boletins',
            'objetos_transportes',
        ]

    objeto_usuario = UsuarioSerializer(
        many=False,
        source='usuario',
        read_only=True,
    )
    objetos_telefones = TelefonePessoaSerializer(
        many=True,
        source='pessoa_telefones',
        read_only=True,
    )
    objetos_emails = EmailPessoaSerializer(
        many=True,
        source='pessoa_emails',
        read_only=True,
    )
    objetos_responsaveis = ResponsavelSerializer(
        many=True,
        source='aluno_responsaveis',
        read_only=True,
    )
    objetos_boletins = BoletimSerializer(
        many=True,
        source='aluno_boletins',
        read_only=True,
    )
    objetos_transportes = TransporteSerializer(
        many=True,
        source='alunos_transportes',
        read_only=True,
    )