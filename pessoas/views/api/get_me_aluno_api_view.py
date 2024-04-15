from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pessoas.models import Aluno
from pessoas.permissions import IsAluno, GetPermission
from pessoas.serializers import AlunoSerializer, UsuarioSerializer


class GetMeAluno(APIView):
    permission_classes = [
        IsAluno, GetPermission,
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
            aluno = get_object_or_404(Aluno, usuario__username=username)
            if aluno:
                serializer = AlunoSerializer(aluno)

        return Response(serializer.data, status=status.HTTP_200_OK)
