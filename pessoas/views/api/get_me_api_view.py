from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pessoas.models import Funcionario
from pessoas.permissions import IsFuncionario
from pessoas.serializers import FuncionarioSerializer, UsuarioSerializer


class GetMe(APIView):
    """
    Uma API para recuperar informações do usuário logado.

    Esta API permite que um funcionário recupere suas próprias informações com base no nome de usuário fornecido.
    """
    permission_classes = [
        IsFuncionario,  # Permissão necessária para que apenas funcionários possam acessar esta API
    ]

    @staticmethod
    def post(request, *args, **kwargs):
        """
        Método para lidar com solicitações POST para recuperar informações do usuário logado.

        Retorna as informações do usuário logado com base no nome de usuário fornecido na solicitação.
        """
        username = request.data.get('username')

        if not username:
            # Se o campo "username" estiver faltando no corpo da solicitação, retorna um erro 400
            return Response(
                {'error': 'O campo "username" é obrigatório no corpo da requisição.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Busca o usuário com base no nome de usuário fornecido
        usuario = get_object_or_404(User, username=username)
        if usuario.is_superuser:
            # Se o usuário é um superusuário, serializa as informações de usuário
            serializer = UsuarioSerializer(usuario)
        else:
            # Se o usuário não é um superusuário, busca o registro de funcionário associado
            funcionario = get_object_or_404(Funcionario, usuario__username=username)
            # Serializa as informações do funcionário
            serializer = FuncionarioSerializer(funcionario)

        return Response(serializer.data, status=status.HTTP_200_OK)
