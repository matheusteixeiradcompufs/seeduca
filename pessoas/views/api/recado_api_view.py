from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from pessoas.models import Recado
from pessoas.serializers import RecadoSerializer


class RecadoViewSet(viewsets.ModelViewSet):
    """
    Uma viewset para visualizar e editar recados.

    Esta viewset fornece operações CRUD (Create, Retrieve, Update, Destroy) para recados.
    """
    queryset = Recado.objects.all()  # Define o conjunto de consultas como todos os recados
    serializer_class = RecadoSerializer  # Define a classe serializadora como RecadoSerializer
    permission_classes = [
        AllowAny,  # Permissão que permite acesso a qualquer usuário, independente de autenticação
    ]
