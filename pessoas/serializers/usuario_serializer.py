from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from pessoas.serializers.pessoa_serializer import PessoaSerializer


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
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
            'is_superuser',
            'groups',
            'objetos_grupos',
            'objeto_pessoa',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    objetos_grupos = GrupoSerializer(
        many=True,
        source='groups',
        read_only=True,
    )
    objeto_pessoa = PessoaSerializer(
        many=False,
        source='usuario_pessoa',
        read_only=True,
    )

    def create(self, validated_data):
        # Hash da senha antes de salvar o usuário
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Verifique se 'password' está presente em validated_data e não é vazio
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)