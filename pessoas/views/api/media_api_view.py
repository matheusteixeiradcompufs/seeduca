from rest_framework import viewsets
from pessoas.models import Media
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import MediaSerializer


class MediaViewSet(viewsets.ModelViewSet):
    """
    Uma viewset para visualizar e editar mídias.

    Esta viewset fornece operações CRUD (Create, Retrieve, Update, Destroy) para mídias.
    """
    queryset = Media.objects.all()  # Define o conjunto de consultas como todas as mídias
    serializer_class = MediaSerializer  # Define a classe serializadora como MediaSerializer
    permission_classes = [
        CoordenadorFullPermission,  # Permissão necessária para coordenadores acessarem esta viewset
    ]
