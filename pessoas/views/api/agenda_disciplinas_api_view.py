from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import AgendaDisciplinasSerializer


class AgendaDisciplinas(APIView):
    permission_classes = [
        CoordenadorFullPermission,
    ]

    def post(self, request, *args, **kwargs):
        serializer = AgendaDisciplinasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Disciplinas adicionadas com sucesso."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
