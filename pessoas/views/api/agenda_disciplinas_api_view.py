from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pessoas.permissions import ProfessorCreateUpdatePermission
from pessoas.serializers import AgendaDisciplinasSerializer


class AgendaDisciplinas(APIView):
    """
    Uma API view para adicionar disciplinas à agenda escolar.

    Requer permissões de criação e atualização de professores.
    """
    permission_classes = [
        ProfessorCreateUpdatePermission,  # Permissão necessária para professores
    ]

    @staticmethod
    def post(request, *args, **kwargs):
        """
        Método para adicionar disciplinas à agenda escolar.

        Requer um pedido POST com dados serializados da disciplina.

        Retorna uma mensagem de sucesso se as disciplinas forem adicionadas com sucesso.
        Caso contrário, retorna uma resposta com erros de validação.
        """
        serializer = AgendaDisciplinasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Disciplinas adicionadas com sucesso."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)