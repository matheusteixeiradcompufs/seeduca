from rest_framework import viewsets

from escolas.models import Tarefa
from escolas.serializers import TarefaSerializer
from pessoas.permissions import ProfessorCreateUpdatePermission


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [
        ProfessorCreateUpdatePermission,
    ]