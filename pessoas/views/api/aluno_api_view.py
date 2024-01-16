from rest_framework import viewsets

from pessoas.models import Aluno
from pessoas.permissions import AlunoPermission
from pessoas.serializers import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [
        # AlunoPermission,
    ]