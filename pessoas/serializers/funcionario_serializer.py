from rest_framework import serializers

from escolas.serializers import EscolaSerializer, TurmaSerializer
from pessoas.models import Funcionario
from pessoas.serializers.telefone_pessoa_serializer import TelefonePessoaSerializer
from pessoas.serializers.email_pessoa_serializer import EmailPessoaSerializer
from pessoas.serializers.usuario_serializer import UsuarioSerializer, criar_usuario, atualizar_usuario


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'endereco',
            'criado_em',
            'atualizado_em',
            'escolas',
            'formacao',
            'retrato',
            'turmas',
            'objeto_usuario',
            'objetos_escolas',
            'objetos_telefones',
            'objetos_emails',
            'objetos_turmas',
        ]

    objeto_usuario = UsuarioSerializer(
        many=False,
        source='usuario',
    )
    objetos_escolas = EscolaSerializer(
        many=True,
        source='escola',
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
    objetos_turmas = TurmaSerializer(
        many=True,
        source='turmas',
        read_only=True,
    )

    def create(self, validated_data):

        # Atualize os campos diretamente em `usuario`
        grupos_add = self.initial_data.pop('grupos_add', [])

        usuario_data = validated_data.pop('usuario', {})

        usuario_data['grupos_add'] = grupos_add

        return criar_usuario(Funcionario, validated_data, usuario_data)

    def update(self, instance, validated_data):

        # Atualize os campos diretamente em `usuario`
        grupos_add = self.initial_data.pop('grupos_add', [])
        grupos_remove = self.initial_data.pop('grupos_remove', [])

        usuario_data = validated_data.pop('usuario', {})

        usuario_data['grupos_add'] = grupos_add
        usuario_data['grupos_remove'] = grupos_remove

        instance = atualizar_usuario(instance, validated_data, usuario_data)

        return super(FuncionarioSerializer, self).update(instance, validated_data)