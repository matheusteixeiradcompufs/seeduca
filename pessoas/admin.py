from django.contrib import admin
from pessoas.models import Aluno, TelefonePessoa, EmailPessoa, Funcionario, Boletim, Avaliacao, Frequencia, DiaLetivo, \
    Transporte, TelefoneTransporte, Media, AgendaRecados, Recado, Situacao


class TelefoneTransporteInline(admin.TabularInline):
    """
    Inline para a model TelefoneTransporte.

    Esta inline é usada para exibir e editar informações sobre os telefones associados aos transportes.

    Atributos:
        model (class): A model associada aos telefones do transporte.
        extra (int): O número de formulários de telefone adicionais exibidos para edição.
    """
    model = TelefoneTransporte
    extra = 1


@admin.register(Transporte)
class TransporteAdmin(admin.ModelAdmin):
    """
    Admin para a model Transporte.

    Este admin é usado para exibir e editar informações sobre os transportes.

    Atributos:
        inlines (list): Uma lista das inlines associadas à model Transporte.
    """
    inlines = [TelefoneTransporteInline, ]


class TelefonePessoaInline(admin.TabularInline):
    """
    Inline para a model TelefonePessoa.

    Esta inline é usada para exibir e editar informações sobre os telefones associados às pessoas.

    Atributos:
        model (class): A model associada aos telefones das pessoas.
        extra (int): O número de formulários de telefone adicionais exibidos para edição.
    """
    model = TelefonePessoa
    extra = 1


class EmailPessoaInline(admin.TabularInline):
    """
    Inline para a model EmailPessoa.

    Esta inline é usada para exibir e editar informações sobre os emails associados às pessoas.

    Atributos:
        model (class): A model associada aos emails das pessoas.
        extra (int): O número de formulários de email adicionais exibidos para edição.
    """
    model = EmailPessoa
    extra = 1


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    """
    Admin para a model Funcionario.

    Este admin é usado para exibir e editar informações sobre os funcionários.

    Atributos:
        list_display (tuple): Uma tupla dos campos exibidos na lista de funcionários.
        inlines (list): Uma lista das inlines associadas à model Funcionario.
    """
    list_display = ('id', '__str__', )
    inlines = [TelefonePessoaInline, EmailPessoaInline]


class BoletimInline(admin.TabularInline):
    """
    Inline para a model Boletim.

    Esta inline é usada para exibir e editar informações sobre os boletins associados aos alunos.

    Atributos:
        model (class): A model associada aos boletins dos alunos.
        extra (int): O número de formulários de boletim adicionais exibidos para edição.
    """
    model = Boletim
    extra = 1


class AgendaRecadosInline(admin.TabularInline):
    """
    Inline para a model AgendaRecados.

    Esta inline é usada para exibir e editar informações sobre os recados associados aos boletins dos alunos.

    Atributos:
        model (class): A model associada aos recados dos boletins dos alunos.
        extra (int): O número de formulários de recado adicionais exibidos para edição.
    """
    model = AgendaRecados
    extra = 1


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    """
    Admin para a model Aluno.

    Este admin é usado para exibir e editar informações sobre os alunos.

    Atributos:
        list_display (tuple): Uma tupla dos campos exibidos na lista de alunos.
        inlines (list): Uma lista das inlines associadas à model Aluno.
    """
    list_display = ('id', '__str__', )
    inlines = [TelefonePessoaInline, EmailPessoaInline, BoletimInline]


class AvaliacaoInline(admin.TabularInline):
    """
    Inline para a model Avaliacao.

    Esta inline é usada para exibir e editar informações sobre as avaliações associadas aos boletins dos alunos.

    Atributos:
        model (class): A model associada às avaliações dos boletins dos alunos.
        extra (int): O número de formulários de avaliação adicionais exibidos para edição.
    """
    model = Avaliacao
    extra = 0


class MediaInline(admin.TabularInline):
    """
    Inline para a model Media.

    Esta inline é usada para exibir e editar informações sobre as médias calculadas para os boletins dos alunos.

    Atributos:
        model (class): A model associada às médias dos boletins dos alunos.
        extra (int): O número de formulários de média adicionais exibidos para edição.
    """
    model = Media
    extra = 0


class SituacaoInline(admin.TabularInline):
    """
    Inline para a model Situacao.

    Esta inline é usada para exibir e editar informações sobre as situações associadas aos boletins dos alunos.

    Atributos:
        model (class): A model associada às situações dos boletins dos alunos.
        extra (int): O número de formulários de situação adicionais exibidos para edição.
    """
    model = Situacao
    extra = 0


class FrequenciaInline(admin.TabularInline):
    """
    Inline para a model Frequencia.

    Esta inline é usada para exibir e editar informações sobre as frequências dos alunos.

    Atributos:
        model (class): A model associada às frequências dos alunos.
        extra (int): O número de formulários de frequência adicionais exibidos para edição.
    """
    model = Frequencia
    extra = 0


@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    """
    Admin para a model Boletim.

    Este admin é usado para exibir e editar informações sobre os boletins dos alunos.

    Atributos:
        inlines (list): Uma lista das inlines associadas à model Boletim.
    """
    inlines = [FrequenciaInline, AvaliacaoInline, MediaInline, SituacaoInline, AgendaRecadosInline]


class DiaLetivoInline(admin.TabularInline):
    """
    Inline para a model DiaLetivo.

    Esta inline é usada para exibir e editar informações sobre os dias letivos associados às frequências dos alunos.

    Atributos:
        model (class): A model associada aos dias letivos das frequências dos alunos.
        extra (int): O número de formulários de dia letivo adicionais exibidos para edição.
    """
    model = DiaLetivo
    extra = 1


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    """
    Admin para a model Frequencia.

    Este admin é usado para exibir e editar informações sobre as frequências dos alunos.

    Atributos:
        inlines (list): Uma lista das inlines associadas à model Frequencia.
    """
    inlines = [DiaLetivoInline, ]


class RecadoInline(admin.TabularInline):
    """
    Inline para a model Recado.

    Esta inline é usada para exibir e editar informações sobre os recados associados às agendas de recados.

    Atributos:
        model (class): A model associada aos recados das agendas de recados.
        extra (int): O número de formulários de recado adicionais exibidos para edição.
    """
    model = Recado
    extra = 1


@admin.register(AgendaRecados)
class AgendaRecadosAdmin(admin.ModelAdmin):
    """
    Admin para a model AgendaRecados.

    Este admin é usado para exibir e editar informações sobre as agendas de recados.

    Atributos:
        inlines (list): Uma lista das inlines associadas à model AgendaRecados.
    """
    inlines = [RecadoInline, ]


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    """
    Admin para a model Avaliacao.

    Este admin é usado para exibir e editar informações sobre as avaliações.

    Atributos:
        list_display (tuple): Uma tupla dos campos exibidos na lista de avaliações.
        list_filter (list): Uma lista dos campos pelos quais a lista de avaliações pode ser filtrada.
    """
    list_display = ['__str__', 'disciplina']
    list_filter = ['nome', 'disciplina']
