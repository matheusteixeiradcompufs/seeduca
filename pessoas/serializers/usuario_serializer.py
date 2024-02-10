from django.contrib.auth.models import Group, User
from rest_framework import serializers


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
            'groups',
            'objetos_grupos',
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