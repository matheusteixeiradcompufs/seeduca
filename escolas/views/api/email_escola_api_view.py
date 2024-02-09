from rest_framework import viewsets

from escolas.models import EmailEscola
from escolas.serializers import EmailEscolaSerializer
from pessoas.permissions import DiretorEscolaPermission


class EmailEscolaViewSet(viewsets.ModelViewSet):
    queryset = EmailEscola.objects.all()
    serializer_class = EmailEscolaSerializer
    permission_classes = [
        # DiretorEscolaPermission,
    ]