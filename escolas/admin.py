from django.contrib import admin
from django.contrib.admin import ModelAdmin

from escolas.models import Escola, TelefoneEscola, EmailEscola, Turma, Sala, AgendaEscolar, Disciplina, DiaAgenda, \
    Aviso, Tarefa, \
    CardapioMerenda, ItemCardapioMerenda, MuralAvisos, AvisoEscola


class TelefoneInline(admin.TabularInline):
    model = TelefoneEscola
    extra = 1


class EmailInline(admin.TabularInline):
    model = EmailEscola
    extra = 1


class CardapioMerendaInline(admin.TabularInline):
    model = CardapioMerenda
    extra = 1


@admin.register(Escola)
class EscolaAdmin(ModelAdmin):
    inlines = [TelefoneInline, EmailInline, CardapioMerendaInline, ]


class DiaAgendaInline(admin.TabularInline):
    model = DiaAgenda
    extra = 1


@admin.register(AgendaEscolar)
class AgendaEscolarAdmin(ModelAdmin):
    inlines = [DiaAgendaInline, ]


class AvisoInline(admin.TabularInline):
    model = Aviso
    extra = 1


class TarefaInline(admin.TabularInline):
    model = Tarefa
    extra = 1


@admin.register(DiaAgenda)
class DiaAgendaAdmin(ModelAdmin):
    inlines = [AvisoInline, TarefaInline, ]


@admin.register(Sala)
class SalaAdmin(ModelAdmin):
    list_display = ("__str__", "escola")
    list_filter = ("numero", "escola")


@admin.register(Disciplina)
class DisciplinaAdmin(ModelAdmin):
    ...


class AgendaInLine(admin.TabularInline):
    model = AgendaEscolar
    extra = 1


@admin.register(Turma)
class TurmaAdmin(ModelAdmin):
    inlines = [AgendaInLine, ]
    list_display = ("__str__", 'sala', 'ano', "sala_escola")
    list_filter = ("nome", 'sala', "ano", "sala__escola")

    def sala_escola(self, obj):
        return obj.sala.escola

    sala_escola.short_description = 'Escola'


@admin.register(CardapioMerenda)
class CardapioMerendaAdmin(ModelAdmin):
    ...


@admin.register(ItemCardapioMerenda)
class ItemCardapioMerendaAdmin(ModelAdmin):
    ...


class AvisoEscolaInline(admin.TabularInline):
    model = AvisoEscola
    extra = 0


@admin.register(MuralAvisos)
class MuralAvisosAdmin(ModelAdmin):
    inlines = [AvisoEscolaInline, ]
