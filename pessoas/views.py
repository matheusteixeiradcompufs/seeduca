from rest_framework import viewsets

from pessoas.models import Aluno, Funcionario
from pessoas.serializers import AlunoSerializer, FuncionarioSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # permission_classes = [
    #     AlunoPermission,
    # ]


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    # permission_classes = [
    #     FuncionarioPermission,
    # ]