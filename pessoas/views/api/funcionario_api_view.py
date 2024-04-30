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

        elif not user.groups.filter(name__in=['Professor', 'Coordenador', 'Diretor']).exists():
            # Se o usuário é um superusuário, retorna todos os registros
            return Funcionario.objects.none()

        elif user.groups.filter(name='Professor').exists():
            # Se o usuário é um Professor, retorna apenas seu próprio registro
            return Funcionario.objects.filter(usuario=user)

        elif user.groups.filter(name='Coordenador').exists():
            # Se o usuário é um Coordenador, retorna seu próprio registro e registros de Professores
            return Funcionario.objects.filter(usuario=user) | Funcionario.objects.filter(
                usuario__groups__name='Professor')

        else:
            # Se o usuário é um Diretor, retorna seu próprio registro e registros de Coordenadores e Professores
            return Funcionario.objects.filter(usuario=user) | Funcionario.objects.filter(
                usuario__groups__name__in=['Coordenador', 'Professor'])