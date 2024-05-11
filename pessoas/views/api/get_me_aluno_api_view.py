from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pessoas.models import Aluno
from pessoas.permissions import IsAluno
from pessoas.serializers.app.app_aluno_serializer import AppAlunoSerializer


class GetMeAluno(APIView):
    """
    Uma API para recuperar informações do aluno associado a um usuário.

    Esta API permite que um aluno recupere suas próprias informações com base no nome de usuário fornecido.
    """
    permission_classes = [
        IsAluno,  # Permissão necessária para que apenas alunos possam acessar esta API
    ]

    @staticmethod
    def post(request, *args, **kwargs):
        """
        Método para lidar com solicitações POST para recuperar informações do aluno.

        Retorna as informações do aluno associado ao nome de usuário fornecido na solicitação.
        """
        username = request.data.get('username')

        if not username:
            # Se o campo "username" estiver faltando no corpo da solicitação, retorna um erro 400
            return Response(
                {'error': 'O campo "username" é obrigatório no corpo da requisição.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Busca o aluno associado ao nome de usuário fornecido
        aluno = get_object_or_404(Aluno, usuario__username=username)
        # Serializa os dados do aluno encontrado
        serializer = AppAlunoSerializer(aluno)

        return Response(serializer.data, status=status.HTTP_200_OK)
