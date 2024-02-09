from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pessoas.models import Aluno
from pessoas.permissions import IsAluno
from pessoas.serializers import AlunoSerializer


class GetMe(APIView):
    permission_classes = [
        # IsAluno,
    ]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')

        if not username:
            return Response(
                {'error': 'O campo "username" é obrigatório no corpo da requisição.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        aluno = get_object_or_404(Aluno, usuario__username=username)

        serializer = AlunoSerializer(aluno)

        return Response(serializer.data, status=status.HTTP_200_OK)
