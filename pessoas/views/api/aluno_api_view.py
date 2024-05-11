from rest_framework import viewsets
from pessoas.models import Aluno
from pessoas.permissions import AlunoPermission
from pessoas.serializers import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para exibir e manipular informações dos alunos.

    Esta ViewSet permite a exibição, criação, atualização e exclusão de informações sobre os alunos.

    Requer permissões específicas para acessar as informações dos alunos.
    """
    queryset = Aluno.objects.all()  # Define o conjunto de consultas para todos os objetos Aluno
    serializer_class = AlunoSerializer  # Define o serializador usado para a serialização e desserialização
    permission_classes = [
        AlunoPermission,  # Permissão necessária para acessar informações dos alunos
    ]
