from rest_framework import viewsets

from pessoas.models import Media
from pessoas.permissions import CoordenadorFullPermission
from pessoas.serializers import MediaSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [
        CoordenadorFullPermission,
    ]