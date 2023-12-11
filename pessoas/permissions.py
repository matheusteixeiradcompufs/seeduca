from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions


class AlunoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' and not request.user.groups.exists():
            aluno_id = view.kwargs.get('pk')
            return str(request.user.usuario_pessoa.id) == str(aluno_id)
        elif request.method == 'GET' and request.user.groups.filter(name='Professores').exists():
            return request.user.is_authenticated
        elif request.user.groups.filter(name__in=['Coordenadores', 'Diretores']).exists():
            return request.user.is_authenticated
        return request.user.is_superuser


class FuncionarioPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        user = request.user

        if request.method == 'POST':
            if user.groups.filter(name='Professores').exists():
                return False

            elif user.groups.filter(name='Coordenadores').exists():
                grupos = request.data.get('grupos_add', [])
                return len(grupos) == 1 and 'Professores' in grupos and 'Coordenadores' not in grupos and 'Diretores' not in grupos

            elif user.groups.filter(name='Diretores').exists():
                grupos = request.data.get('grupos_add', [])
                return len(grupos) == 1 and ('Professores' in grupos or 'Coordenadores' in grupos) and 'Diretores' not in grupos

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        usuario = request.user

        if usuario.is_superuser:
            return usuario.is_superuser

        if request.method == 'GET' and obj is not None:
            if usuario.groups.filter(name='Professores').exists():
                return usuario == obj.usuario

            elif usuario.groups.filter(name='Coordenadores').exists():
                if obj.usuario.groups.filter(name='Coordenadores').exists():
                    return usuario == obj.usuario
                else:
                    return obj.usuario.groups.filter(name='Professores').exists()

            elif usuario.groups.filter(name='Diretores').exists():
                if obj.usuario.groups.filter(name='Diretores').exists():
                    return usuario == obj.usuario
                else:
                    return obj.usuario.groups.filter(name__in=['Professores', 'Coordenadores']).exists()

        elif request.method == 'PATCH':
            grupos = request.data.get('grupos_add', [])
            if usuario.groups.filter(name='Coordenadores').exists() and obj.usuario.groups.filter(name='Professores').exists():
                if len(grupos) == 0:
                    return True
                else:
                    return len(grupos) == 1 and 'Professores' in grupos and 'Coordenadores' not in grupos and 'Diretores' not in grupos

            elif usuario.groups.filter(name='Diretores').exists() and (obj.usuario.groups.filter(name='Professores').exists() or obj.usuario.groups.filter(name='Coordenadores').exists()):
                if len(grupos) == 0:
                    return True
                else:
                    return len(grupos) == 1 and ('Professores' in grupos or 'Coordenadores' in grupos) and 'Diretores' not in grupos

        elif request.method == 'DELETE':
            return (usuario.groups.filter(name='Coordenadores').exists() and obj.usuario.groups.filter(name='Professores').exists()) or (usuario.groups.filter(name='Diretores').exists() and (obj.usuario.groups.filter(name='Professores').exists() or obj.usuario.groups.filter(name='Coordenadores').exists()))
