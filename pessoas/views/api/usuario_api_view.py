from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from pessoas.serializers import UsuarioSerializer, GrupoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet que fornece operações CRUD para usuários.

    Esta ViewSet permite que todos os usuários acessem e gerenciem informações sobre usuários.
    Os métodos CRUD (Create, Retrieve, Update, Delete) estão disponíveis nesta ViewSet.

    Os usuários não autenticados também têm permissão para acessar esta ViewSet.

    """
    queryset = User.objects.all()  # Obtém todos os objetos de Usuário do banco de dados
    serializer_class = UsuarioSerializer  # Define a classe de serializador para Usuário
    permission_classes = [
        AllowAny,  # Permite que usuários não autenticados acessem esta ViewSet
    ]


class GrupoViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet que fornece operações CRUD para grupos.

    Esta ViewSet permite que usuários autenticados acessem e gerenciem informações sobre grupos.
    Os métodos CRUD (Create, Retrieve, Update, Delete) estão disponíveis nesta ViewSet.

    """
    queryset = Group.objects.all()  # Obtém todos os objetos de Grupo do banco de dados
    serializer_class = GrupoSerializer  # Define a classe de serializador para Grupo
    permission_classes = [
        # Nenhuma permissão específica definida, portanto, apenas usuários autenticados têm acesso
    ]
