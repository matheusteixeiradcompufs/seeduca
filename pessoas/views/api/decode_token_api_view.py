import jwt
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from jwt.exceptions import InvalidTokenError

from appseeduca import settings


class DecodeTokenAPIView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request):
        token = request.GET.get('token')
        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                return Response(payload, status=200)
            # except jwt.ExpiredSignatureError:
            #     return Response({'error': 'Token expirado'}, status=400)
            except InvalidTokenError:
                return Response({'error': 'Token inválido'}, status=400)
            # except Exception as e:
            #     return Response({'error': f'Erro ao decodificar o token: {str(e)}'}, status=400)
        else:
            return Response({'error': 'Parâmetro "token" não encontrado na requisição'}, status=400)
