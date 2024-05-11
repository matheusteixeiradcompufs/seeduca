from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from pessoas.serializers.pessoa_serializer import PessoaSerializer


class GrupoSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Group.
    """
    class Meta:
        model = Group
        fields = [
            'id',    # ID do grupo
            'name',  # Nome do grupo
        ]


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos User.
    """
    class Meta:
        model = User
        fields = [
            'id',            # ID do usuário
            'username',      # Nome de usuário
            'first_name',    # Primeiro nome do usuário
            'last_name',     # Sobrenome do usuário
            'email',         # Email do usuário
            'password',      # Senha do usuário
            'is_superuser',  # Indica se o usuário é um superusuário
            'groups',        # Grupos associados ao usuário
            'objetos_grupos',  # Objetos serializados dos grupos associados
            'objeto_pessoa',   # Objeto serializado da pessoa associada
        ]
        extra_kwargs = {
            'password': {
                'write_only': True  # A senha só pode ser escrita e não retornada nas consultas
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
        """
        Método para criar um novo usuário.
        """
        # Hash da senha antes de salvar o usuário
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Método para atualizar um usuário existente.
        """
        # Verifique se 'password' está presente em validated_data e não é vazio
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        else:
            pass
        return super().update(instance, validated_data)
