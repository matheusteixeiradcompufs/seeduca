from django.contrib import admin
from django.contrib.admin import ModelAdmin

from escolas.models import Escola, TelefoneEscola, EmailEscola, Turma, Sala, AgendaEscolar, Disciplina, DiaAgenda, \
    Aviso, Tarefa, \
    CardapioMerenda, ItemCardapioMerenda, MuralAvisos, AvisoEscola


class TelefoneInline(admin.TabularInline):
    """
    Inline admin para adicionar e editar telefones de uma escola.
    """
    model = TelefoneEscola
    extra = 1


class EmailInline(admin.TabularInline):
    """
    Inline admin para adicionar e editar emails de uma escola.
    """
    model = EmailEscola
    extra = 1


class CardapioMerendaInline(admin.TabularInline):
    """
    Inline admin para adicionar e editar cardápios de merenda de uma escola.
    """
    model = CardapioMerenda
    extra = 1


@admin.register(Escola)
class EscolaAdmin(ModelAdmin):
    """
    Administração de escolas.
    """
    inlines = [TelefoneInline, EmailInline, CardapioMerendaInline, ]


class DiaAgendaInline(admin.TabularInline):
    """
    Inline admin para adicionar e editar dias na agenda escolar.
    """
    model = DiaAgenda
    extra = 1


@admin.register(AgendaEscolar)
class AgendaEscolarAdmin(ModelAdmin):
    """
    Administração de agendas escolares.
    """
    inlines = [DiaAgendaInline, ]


class AvisoInline(admin.TabularInline):
    """
    Inline admin para adicionar e editar avisos em um dia da agenda escolar.
    """
    model = Aviso
    extra = 1


class TarefaInline(admin.TabularInline):
    """
    Inline admin para adicionar e editar tarefas em um dia da agenda escolar.
    """
    model = Tarefa
    extra = 1


@admin.register(DiaAgenda)
class DiaAgendaAdmin(ModelAdmin):
    """
    Administração de dias na agenda escolar.
    """
    inlines = [AvisoInline, TarefaInline, ]


@admin.register(Sala)
class SalaAdmin(ModelAdmin):
    """
    Administração de salas de aula.
    """
    list_display = ("__str__", "escola")
    list_filter = ("numero", "escola")


@admin.register(Disciplina)
class DisciplinaAdmin(ModelAdmin):
    """
    Administração de disciplinas escolares.
    """
    ...


class AgendaInLine(admin.TabularInline):
    """
    Inline admin para adicionar e editar agendas escolares em uma turma.
    """
    model = AgendaEscolar
    extra = 1


@admin.register(Turma)
class TurmaAdmin(ModelAdmin):
    """
    Administração de turmas escolares.
    """
    inlines = [AgendaInLine, ]
    list_display = ("__str__", 'sala', 'ano')
    list_filter = ("nome", 'sala', "ano", "sala__escola")


@admin.register(CardapioMerenda)
class CardapioMerendaAdmin(ModelAdmin):
    """
    Administração de cardápios de merenda.
    """
    ...


@admin.register(ItemCardapioMerenda)
class ItemCardapioMerendaAdmin(ModelAdmin):
    """
    Administração de itens de cardápio de merenda.
    """
    ...


class AvisoEscolaInline(admin.TabularInline):
    """
    Inline admin para adicionar e editar avisos em um mural de avisos de uma escola.
    """
    model = AvisoEscola
    extra = 0


@admin.register(MuralAvisos)
class MuralAvisosAdmin(ModelAdmin):
    """
    Administração de murais de avisos escolares.
    """
    inlines = [AvisoEscolaInline, ]
