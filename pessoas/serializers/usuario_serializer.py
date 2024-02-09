from django.contrib.auth.models import Group, User
from rest_framework import serializers


# def criar_usuario(classe, classe_data, usuario_data):
#     usuario_serializer = UsuarioSerializer(data=usuario_data)
#     if usuario_serializer.is_valid():
#         usuario = usuario_serializer.save()
#
#         usuario_classe = classe.objects.create(usuario=usuario, **classe_data)
#         return usuario_classe
#
#
# def atualizar_usuario(instance, validated_data, usuario_data):
#     usuario_serializer = UsuarioSerializer(instance=instance.usuario, data=usuario_data, partial=True)
#     if usuario_serializer.is_valid():
#         usuario_serializer.save()
#
#     for key, value in validated_data.items():
#         setattr(instance, key, value)
#
#     instance.save()
#
#     return instance


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
    #
    # def create(self, validated_data):
    #
    #     grupos = self.initial_data.pop('grupos_add', [])
    #
    #     user = User.objects.create_user(**validated_data)
    #
    #     for grupo_nome in grupos:
    #         grupo = Group.objects.get(name=grupo_nome)
    #         user.groups.add(grupo)
    #
    #     return user
    #
    # def update(self, instance, validated_data):
    #
    #     grupos_add = self.initial_data.pop('grupos_add', [])
    #
    #     for grupo_nome in grupos_add:
    #         grupo = Group.objects.get(name=grupo_nome)
    #         instance.groups.add(grupo)
    #
    #     grupos_remove = self.initial_data.pop('grupos_remove', [])
    #
    #     for grupo_nome in grupos_remove:
    #         grupo = Group.objects.get(name=grupo_nome)
    #         instance.groups.remove(grupo)
    #
    #     return super(UsuarioSerializer, self).update(instance, validated_data)