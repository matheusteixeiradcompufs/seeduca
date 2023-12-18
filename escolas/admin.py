from django.contrib import admin
from django.contrib.admin import ModelAdmin

from escolas.models import Escola, TelefoneEscola, EmailEscola, Turma, Sala, AgendaEscolar, Disciplina, DiaAgenda, Aviso, Tarefa, \
    CardapioMerenda, ItemCardapioMerenda


class TelefoneInline(admin.TabularInline):
    model = TelefoneEscola
    extra = 1


class EmailInline(admin.TabularInline):
    model = EmailEscola
    extra = 1


@admin.register(Escola)
class EscolaAdmin(ModelAdmin):
    inlines = [TelefoneInline, EmailInline, ]


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


class CardapioMerendaInline(admin.TabularInline):
    model = CardapioMerenda
    extra = 1


@admin.register(DiaAgenda)
class SalaAdmin(ModelAdmin):
    inlines = [AvisoInline, TarefaInline, CardapioMerendaInline, ]


@admin.register(Sala)
class SalaAdmin(ModelAdmin):
    ...


@admin.register(Disciplina)
class DisciplinaAdmin(ModelAdmin):
    ...


@admin.register(Turma)
class TurmaAdmin(ModelAdmin):
    ...


@admin.register(CardapioMerenda)
class CardapioMerendaAdmin(ModelAdmin):
    ...


@admin.register(ItemCardapioMerenda)
class ItemCardapioMerendaAdmin(ModelAdmin):
    ...
