from rest_framework import viewsets

from escolas.models import Tarefa
from escolas.serializers import TarefaSerializer
from pessoas.permissions import ProfessorCreateUpdatePermission


class TarefaViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de tarefas de um dia de agenda escolar.

    Este endpoint permite listar, criar, atualizar e excluir tarefas.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [
        ProfessorCreateUpdatePermission,
    ]