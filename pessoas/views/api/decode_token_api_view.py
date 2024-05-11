import jwt
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from jwt.exceptions import InvalidTokenError
from appseeduca import settings


class DecodeTokenAPIView(APIView):
    """
    Uma API view para decodificar tokens JWT.

    Esta view permite decodificar um token JWT fornecido nos parâmetros da consulta.
    """
    permission_classes = [
        AllowAny,  # Permissão para permitir acesso a todos, mesmo usuários não autenticados
    ]

    @staticmethod
    def get(request):
        """
        Método para decodificar um token JWT.

        Retorna os dados decodificados do token se ele for válido.
        Retorna uma mensagem de erro se o token for inválido ou se não for fornecido.
        """
        token = request.GET.get('token')  # Obtém o token JWT dos parâmetros da consulta
        if token:
            try:
                # Decodifica o token JWT usando a chave secreta do projeto
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                return Response(payload, status=200)  # Retorna os dados decodificados do token
            except InvalidTokenError:
                return Response({'error': 'Token inválido'}, status=400)  # Retorna um erro se o token for inválido
        else:
            return Response({'error': 'Parâmetro "token" não encontrado na requisição'}, status=400)
            # Retorna um erro se o parâmetro "token" não estiver presente na consulta
