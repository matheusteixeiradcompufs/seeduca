from rest_framework import viewsets

from escolas.models import Aviso
from escolas.serializers import AvisoSerializer
from pessoas.permissions import ProfessorCreateUpdatePermission


class AvisoViewSet(viewsets.ModelViewSet):
    """
    Endpoint para visualização e manipulação de avisos de um dia de agenda escolar.

    Este endpoint permite listar, criar, atualizar e excluir avisos.
    """
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer
    permission_classes = [
        ProfessorCreateUpdatePermission,
    ]