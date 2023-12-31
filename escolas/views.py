from rest_framework import viewsets, permissions

from escolas.models import Escola, Turma, CardapioMerenda, ItemCardapioMerenda, Tarefa, Aviso, DiaAgenda, AgendaEscolar, \
    Sala, Disciplina, EmailEscola, TelefoneEscola
from escolas.permissions import EscolaPermission
from escolas.serializers import EscolaSerializer, TurmaSerializer, CardapioMerendaSerializer, \
    ItemCardapioMerendaSerializer, TarefaSerializer, AvisoSerializer, DiaAgendaSerializer, AgendaEscolarSerializer, \
    SalaSerializer, DisciplinaSerializer, EmailEscolaSerializer, TelefoneEscolaSerializer


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
    permission_classes = [
        EscolaPermission,
    ]


class TelefoneEscolaViewSet(viewsets.ModelViewSet):
    queryset = TelefoneEscola.objects.all()
    serializer_class = TelefoneEscolaSerializer
    permission_classes = []


class EmailEscolaViewSet(viewsets.ModelViewSet):
    queryset = EmailEscola.objects.all()
    serializer_class = EmailEscolaSerializer
    permission_classes = []


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = []


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = []


class AgendaEscolarViewSet(viewsets.ModelViewSet):
    queryset = AgendaEscolar.objects.all()
    serializer_class = AgendaEscolarSerializer
    permission_classes = []


class DiaAgendaViewSet(viewsets.ModelViewSet):
    queryset = DiaAgenda.objects.all()
    serializer_class = DiaAgendaSerializer
    permission_classes = []


class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer
    permission_classes = []


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = []


class ItemCardapioMerendaViewSet(viewsets.ModelViewSet):
    queryset = ItemCardapioMerenda.objects.all()
    serializer_class = ItemCardapioMerendaSerializer
    permission_classes = []


class CardapioMerendaViewSet(viewsets.ModelViewSet):
    queryset = CardapioMerenda.objects.all()
    serializer_class = CardapioMerendaSerializer
    permission_classes = []


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = []



