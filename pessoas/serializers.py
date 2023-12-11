from django.contrib.auth.models import User, Group
from rest_framework import serializers

from escolas.serializers import TelefoneSerializer, EmailSerializer, EscolaSerializer
from pessoas.models import Aluno, Funcionario


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name'
        ]


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
            'grupos',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    grupos = GrupoSerializer(
        many=True,
        source='groups',
        read_only=True,
    )

    def create(self, validated_data):

        grupos = self.initial_data.pop('grupos_add', [])

        user = User.objects.create_user(**validated_data)

        for grupo_nome in grupos:
            grupo = Group.objects.get(name=grupo_nome)
            user.groups.add(grupo)

        return user

    def update(self, instance, validated_data):

        grupos_add = self.initial_data.pop('grupos_add', [])

        for grupo_nome in grupos_add:
            grupo = Group.objects.get(name=grupo_nome)
            instance.groups.add(grupo)

        grupos_remove = self.initial_data.pop('grupos_remove', [])

        for grupo_nome in grupos_remove:
            grupo = Group.objects.get(name=grupo_nome)
            instance.groups.remove(grupo)

        return super(UsuarioSerializer, self).update(instance, validated_data)


def criar_usuario(classe, classe_data, usuario_data):
    usuario_serializer = UsuarioSerializer(data=usuario_data)
    if usuario_serializer.is_valid():
        usuario = usuario_serializer.save()

        usuario_classe = classe.objects.create(usuario=usuario, **classe_data)
        return usuario_classe
    else:
        raise serializers.ValidationError(usuario_serializer.errors)


def atualizar_usuario(instance, validated_data, usuario_data):
    usuario_serializer = UsuarioSerializer(instance=instance.usuario, data=usuario_data, partial=True)
    if usuario_serializer.is_valid():
        usuario_serializer.save()

    # Agora, atualize os campos em `Funcionario`
    for key, value in validated_data.items():
        setattr(instance, key, value)

    instance.save()

    return instance


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
        source='pessoa_telefones',
        read_only=True,
    )
    objetos_emails = EmailSerializer(
        many=True,
        source='pessoa_emails',
        read_only=True,
    )

    def create(self, validated_data):

        usuario_data = validated_data.pop('usuario', {})

        return criar_usuario(Aluno, validated_data, usuario_data)

    def update(self, instance, validated_data):

        usuario_data = validated_data.pop('usuario', {})

        instance = atualizar_usuario(instance, validated_data, usuario_data)

        return super(AlunoSerializer, self).update(instance, validated_data)


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
        source='pessoa_telefones',
        read_only=True,
    )
    objetos_emails = EmailSerializer(
        many=True,
        source='pessoa_emails',
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
