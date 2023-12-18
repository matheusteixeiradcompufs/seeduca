from django.contrib import admin

from pessoas.models import Aluno, EhPCD, TelefonePessoa, EmailPessoa, Funcionario, Boletim, Avaliacao, Frequencia, DiaLetivo, Transporte, TelefoneTransporte


class TelefoneTransporteInline(admin.TabularInline):
    model = TelefoneTransporte
    extra = 1


@admin.register(Transporte)
class TransporteAdmin(admin.ModelAdmin):
    inlines = [TelefoneTransporteInline, ]


class TelefonePessoaInline(admin.TabularInline):
    model = TelefonePessoa
    extra = 1


class EmailPessoaInline(admin.TabularInline):
    model = EmailPessoa
    extra = 1


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', )
    inlines = [TelefonePessoaInline, EmailPessoaInline]


class PCDInline(admin.TabularInline):
    model = EhPCD
    extra = 1


class BoletimInline(admin.TabularInline):
    model = Boletim
    extra = 1


class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', )
    inlines = [TelefonePessoaInline, EmailPessoaInline, PCDInline, BoletimInline, FrequenciaInline]


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]


class DiaLetivoInline(admin.TabularInline):
    model = DiaLetivo
    extra = 1


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    inlines = [DiaLetivoInline, ]
