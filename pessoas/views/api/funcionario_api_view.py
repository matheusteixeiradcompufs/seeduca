from rest_framework import viewsets

from pessoas.models import Funcionario
from pessoas.permissions import FuncionarioPermission
from pessoas.serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [
        FuncionarioPermission,
    ]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            # Se o usuário é um superusuário, retorna todos os registros
            return Funcionario.objects.all()

        if user.groups.filter(name='Professores').exists():
            # Se o usuário é um Professor, retorna apenas seu próprio registro
            return Funcionario.objects.filter(usuario=user)

        if user.groups.filter(name='Coordenadores').exists():
            # Se o usuário é um Coordenador, retorna seu próprio registro e registros de Professores
            return Funcionario.objects.filter(usuario=user) | Funcionario.objects.filter(
                usuario__groups__name='Professores')

        if user.groups.filter(name='Diretores').exists():
            # Se o usuário é um Diretor, retorna seu próprio registro e registros de Coordenadores e Professores
            return Funcionario.objects.filter(usuario=user) | Funcionario.objects.filter(
                usuario__groups__name__in=['Coordenadores', 'Professores'])

        # Se nenhuma condição acima for satisfeita, retorna uma queryset vazia
        return Funcionario.objects.none()