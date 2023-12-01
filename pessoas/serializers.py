from django.contrib.auth.models import User
from rest_framework import serializers

from escolas.serializers import TelefoneSerializer, EmailSerializer, EscolaSerializer
from pessoas.models import Aluno, Funcionario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


def criar_usuario(validated_data, classe):
    usuario_data = validated_data.pop('usuario')
    usuario_serializer = UsuarioSerializer(data=usuario_data)
    if usuario_serializer.is_valid():
        usuario = usuario_serializer.save()
        usuario_classe = classe.objects.create(usuario=usuario, **validated_data)
        return usuario_classe
    else:
        raise serializers.ValidationError(usuario_serializer.errors)


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'endereco',
            'escola',
            'objeto_escola',
            'objeto_usuario',
            'objetos_telefones',
            'objetos_emails',
        ]

    objeto_escola = EscolaSerializer(
        many=False,
        source='escola',
        read_only=True,
    )
    objeto_usuario = UsuarioSerializer(
        many=False,
        source='usuario',
    )
    objetos_telefones = TelefoneSerializer(
        many=True,
        source='telefones',
        read_only=True,
    )
    objetos_emails = EmailSerializer(
        many=True,
        source='emails',
        read_only=True,
    )

    def create(self, validated_data):
        return criar_usuario(validated_data, Aluno)


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'endereco',
            'formacao',
            'escola',
            'objeto_escola',
            'objeto_usuario',
            'objetos_telefones',
            'objetos_emails',
        ]

    objeto_escola = EscolaSerializer(
        many=False,
        source='escola',
        read_only=True,
    )
    objeto_usuario = UsuarioSerializer(
        many=False,
        source='usuario',
    )
    objetos_telefones = TelefoneSerializer(
        many=True,
        source='telefones',
        read_only=True,
    )
    objetos_emails = EmailSerializer(
        many=True,
        source='emails',
        read_only=True,
    )

    def create(self, validated_data):
        return criar_usuario(validated_data, Funcionario)
