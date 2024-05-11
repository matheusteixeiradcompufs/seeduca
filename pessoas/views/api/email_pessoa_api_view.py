from rest_framework import viewsets
from pessoas.models import EmailPessoa
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import EmailPessoaSerializer


class EmailPessoaViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para exibir e manipular informações dos emails das pessoas.

    Esta ViewSet permite a exibição, criação, atualização e exclusão de informações sobre os emails das pessoas.

    Requer permissões específicas para que os coordenadores tenham acesso completo aos emails das pessoas.
    """
    queryset = EmailPessoa.objects.all()  # Define o conjunto de consultas para todos os emails das pessoas
    serializer_class = EmailPessoaSerializer  # Define o serializador usado para a serialização e desserialização
    permission_classes = [
        CoordenadorFullPermission,  # Permissão necessária para que os coordenadores tenham acesso completo aos emails das pessoas
    ]
