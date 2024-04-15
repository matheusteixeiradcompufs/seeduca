from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pessoas.models import Funcionario
from pessoas.permissions import IsFuncionario, GetPermission
from pessoas.serializers import FuncionarioSerializer, UsuarioSerializer


class GetMe(APIView):
    permission_classes = [
        IsFuncionario, GetPermission,
    ]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')

        if not username:
            return Response(
                {'error': 'O campo "username" é obrigatório no corpo da requisição.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        usuario = get_object_or_404(User, username=username)
        if usuario.is_superuser:
            serializer = UsuarioSerializer(usuario)
        else:
            funcionario = get_object_or_404(Funcionario, usuario__username=username)
            if funcionario:
                serializer = FuncionarioSerializer(funcionario)

        return Response(serializer.data, status=status.HTTP_200_OK)
