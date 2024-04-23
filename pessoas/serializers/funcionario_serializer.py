from rest_framework import serializers

from escolas.serializers.turma_sem_objetos_serializer import TurmaSemObjetosSerializer
from pessoas.models import Funcionario
from pessoas.serializers.telefone_pessoa_serializer import TelefonePessoaSerializer
from pessoas.serializers.email_pessoa_serializer import EmailPessoaSerializer
from pessoas.serializers.usuario_serializer import UsuarioSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'endereco',
            'usuario',
            'criado_em',
            'atualizado_em',
            'formacao',
            'retrato',
            'turmas',
            'uid',
            'token',
            'objeto_usuario',
            'objetos_telefones',
            'objetos_emails',
            'objetos_turmas',
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
    objetos_turmas = TurmaSemObjetosSerializer(
        many=True,
        source='turmas',
        read_only=True,
    )
