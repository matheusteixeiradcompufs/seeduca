from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from pessoas.serializers import UsuarioSerializer
from pessoas.serializers.usuario_serializer import GrupoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [

    ]


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [

    ]