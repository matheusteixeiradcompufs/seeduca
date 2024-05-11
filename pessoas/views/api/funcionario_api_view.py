from rest_framework import viewsets
from pessoas.models import Funcionario
from pessoas.permissions import FuncionarioPermission
from pessoas.serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para exibir e manipular informações dos funcionários.

    Esta ViewSet permite a exibição, criação, atualização e exclusão de informações sobre os funcionários.

    Requer permissões específicas para acessar e manipular informações dos funcionários.
    """
    queryset = Funcionario.objects.all()  # Define o conjunto de consultas para todos os funcionários
    serializer_class = FuncionarioSerializer  # Define o serializador usado para a serialização e desserialização
    permission_classes = [
        FuncionarioPermission,  # Permissão necessária para acessar e manipular informações dos funcionários
    ]

    def get_queryset(self):
        """
        Método para filtrar o conjunto de consultas com base no tipo de usuário.

        Retorna um conjunto de consultas filtrado com base no tipo de usuário logado.
        """
        user = self.request.user

        if user.is_superuser:
            # Se o usuário é um superusuário, retorna todos os registros de funcionários
            return Funcionario.objects.all()

        elif not user.groups.filter(name__in=['Professor', 'Coordenador', 'Diretor']).exists():
            # Se o usuário não pertence a nenhum grupo específico, não tem permissão para acessar nenhum registro
            return Funcionario.objects.none()

        elif user.groups.filter(name='Professor').exists():
            # Se o usuário é um Professor, retorna apenas seu próprio registro de funcionário
            return Funcionario.objects.filter(usuario=user)

        elif user.groups.filter(name='Coordenador').exists():
            # Se o usuário é um Coordenador, retorna seu próprio registro e registros de Professores
            return Funcionario.objects.filter(usuario=user) | Funcionario.objects.filter(usuario__groups__name='Professor')

        else:
            # Se o usuário é um Diretor, retorna seu próprio registro e registros de Coordenadores e Professores
            return Funcionario.objects.filter(usuario=user) | Funcionario.objects.filter(usuario__groups__name__in=['Coordenador', 'Professor'])
